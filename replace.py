import os
from PIL import Image

ofile = open('config.in', 'r');
configlist = ofile.readlines()
ofile.close()

cfdic = {}

print '====start===='
print '@@config count : ' + str(len(configlist))

for cfline in configlist:
    cfitem = cfline.split('|');

    width = (cfitem[0])
    height = (cfitem[1])
    path = cfitem[2]
    cfdic[width + '*' + height] = path

for item in cfdic:
    print item, cfdic[item]

for filename in os.listdir('icon'):
    if filename.find('.png') != -1:
        im = Image.open('icon/' + filename)
        iwidth, iheight = im.size;

        print 'PNG : ' + filename,
        print ', width : ' + str(iwidth) + ', height : ' + str(iheight)

        szpath = cfdic[str(iwidth) + '*' + str(iheight)]
        if len(szpath) > 0:
            re = os.system(r'cp icon/%s %s/icon.png' % (filename, szpath))
            if re == 0:
                print '----success----'

        #ofile.close()
        
print '=====end====='
