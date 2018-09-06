import os, time
from tkinter import *


inputDir = 'input\\'
outputDir = 'output\\'
if not os.access(outputDir, os.F_OK):
    os.makedirs(outputDir)
if not os.access(inputDir, os.F_OK):
    os.makedirs(inputDir)


def print_mode(mode):
    print('Run {} Converter'.format(mode), file=logFile)


def run_command(fmtIn, fmtOut, all=False):
    mode = '{}->{}'.format(fmtIn.upper(), fmtOut.upper())
    print_mode(mode)
    startTime = time.time()
    for root, dirs, files in os.walk(inputDir):
        for filePath in files:
            ext = filePath.split(os.extsep)[-1]
            outName = root[len(inputDir): ] + os.sep + filePath[0 : -(len(ext) + 1)]
            if ext == fmtIn:
                if not all:
                    command = 'converter.exe -{0} -{1} {2} -out {3}.{1}'.format(fmtIn, fmtOut, root + os.sep + filePath, outputDir + os.sep + outName)
                else:
                    command = 'converter.exe -{0} -{1} all {2} -out {3}'.format(fmtIn, fmtOut, root + os.sep + filePath, outputDir + os.sep + outName)
                if os.system(command) == 0:
                    print(command, file=logFile)
                else:
                    print(command)
                    print('Error!!! %s not converted' % filePath, file=logFile)
    totalTime = time.time() - startTime
    print('TIME: {}\n'.format(totalTime), file=logFile)
    timer.configure(text='Time: {0:.3}'.format(totalTime))


def ogf_object(event):
    run_command('ogf', 'object')


def ogf_bones(event):
    run_command('ogf', 'bones')


def ogf_skls(event):
    run_command('ogf', 'skls')


def ogf_skl(event):
    run_command('ogf', 'skl', all=True)


def omf_skls(event):
    run_command('omf', 'skls')


def omf_skl(event):
    run_command('omf', 'skl', all=True)


def dm_object(event):
    run_command('dm', 'object')


logFile = open(r'batch_converter.log', 'w')
bgClr = '#808080'
butClr = '#A0A0A0'
actClr = '#B3B3B3'
bw, bh = 13, 1
fontBut = ('Font', 10, 'bold')
fontLab = ('Font', 8, 'bold')
root = Tk()
root.resizable(height=False, width=False)
root.minsize(width=240, height=320)
root.maxsize(width=240, height=320)
root.title('Batch Converter')
root['bg'] = bgClr
x = (root.winfo_screenwidth()) / 2
y = (root.winfo_screenheight()) / 2
root.geometry('+%d+%d' % (x - 120, y - 200))
fr = Frame(root, bg=bgClr, width=240, height=320)
bs1 = '{: <4}-> {: <6}'.format('ogf', 'object')
bs2 = '{: <4}-> {: <6}'.format('ogf', 'bones')
bs3 = '{: <4}-> {: <6}'.format('ogf', 'skls')
bs4 = '{: <4}-> {: <6}'.format('ogf', 'skl')
bs5 = '{: <4}-> {: <6}'.format('omf', 'skls')
bs6 = '{: <4}-> {: <6}'.format('omf', 'skl')
bs7 = '{: <4}-> {: <6}'.format('dm',  'object')
OgfObject = Button(fr, text=bs1, width=bw, height=bh, bg=butClr, activebackground=actClr, font=fontBut)
OgfBones  = Button(fr, text=bs2, width=bw, height=bh, bg=butClr, activebackground=actClr, font=fontBut)
OgfSkls   = Button(fr, text=bs3, width=bw, height=bh, bg=butClr, activebackground=actClr, font=fontBut)
OgfSkl    = Button(fr, text=bs4, width=bw, height=bh, bg=butClr, activebackground=actClr, font=fontBut)
OmfSkls   = Button(fr, text=bs5, width=bw, height=bh, bg=butClr, activebackground=actClr, font=fontBut)
OmfSkl    = Button(fr, text=bs6, width=bw, height=bh, bg=butClr, activebackground=actClr, font=fontBut)
DmObject  = Button(fr, text=bs7, width=bw, height=bh, bg=butClr, activebackground=actClr, font=fontBut)
ver   = Label(fr, text='ver. 0.03',  font=fontLab, bg=bgClr)
date  = Label(fr, text='08.07.2015', font=fontLab, bg=bgClr)
timer = Label(fr, text='',           font=fontLab, bg=bgClr)
fr.grid        (row=0,  column=0, pady=42)
OgfObject.grid (row=4,  column=1, padx=64)
OgfBones.grid  (row=5,  column=1, padx=64)
OgfSkls.grid   (row=6,  column=1, padx=64)
OgfSkl.grid    (row=7,  column=1, padx=64)
OmfSkls.grid   (row=8,  column=1, padx=64)
OmfSkl.grid    (row=9,  column=1, padx=64)
DmObject.grid  (row=10, column=1, padx=64)
timer.grid     (row=11, column=1, padx=64, pady=8)
ver.grid       (row=12, column=1, padx=64)
date.grid      (row=13, column=1, padx=64)
LBM = '<Button-1>'
OgfObject.bind (LBM, ogf_object)
OgfBones.bind  (LBM, ogf_bones)
OgfSkls.bind   (LBM, ogf_skls)
OgfSkl.bind    (LBM, ogf_skl)
OmfSkls.bind   (LBM, omf_skls)
OmfSkl.bind    (LBM, omf_skl)
DmObject.bind  (LBM, dm_object)
root.mainloop()
logFile.close()

