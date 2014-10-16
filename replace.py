import os

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
        ofile = open('icon/' + filename, "rb")
        barray = ofile.read(8 + 25)
        ofile.close()

        iwidth = int(0)
        iheight = int(0)

        for i in range(0, 4):
            iwidth = iwidth + ord(barray[16 + i])
            iwidth = iwidth << 4

            iheight = iheight + ord(barray[16 + 4 + i])
            iheight = iheight << 4

        iwidth = iwidth >> 4
        iheight = iheight >> 4
        print 'PNG : ' + filename,
        print ', width : ' + str(iwidth) + ', height : ' + str(iheight)

        szpath = cfdic[str(iwidth) + '*' + str(iheight)]
        if len(szpath) > 0:
            re = os.system(r'cp icon/%s %s/icon.png' % (filename, szpath))
            if re == 0:
                print '----success----'
        
print '=====end====='
