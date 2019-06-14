import os
import time
import tkinter


INPUT_PATH = 'input'
OUTPUT_PATH = 'output'

if not os.access(OUTPUT_PATH, os.F_OK):
    os.makedirs(OUTPUT_PATH)

if not os.access(INPUT_PATH, os.F_OK):
    os.makedirs(INPUT_PATH)


def print_mode(mode):
    print('Run {} Converter'.format(mode), file=log_file)


def run_command(input_format, output_format, all_option=False):
    mode = '{}->{}'.format(input_format.upper(), output_format.upper())
    print_mode(mode)
    start_time = time.time()

    for root, dirs, files in os.walk(INPUT_PATH):
        for file_path in files:
            ext = file_path.split(os.extsep)[-1]
            out_name = root[len(INPUT_PATH): ] + os.sep + file_path[0 : -(len(ext) + 1)]
            if ext == input_format:
                if not all_option:
                    command = 'converter.exe -{0} -{1} {2} -out {3}.{1}'.format(
                        input_format,
                        output_format,
                        root + os.sep + file_path,
                        OUTPUT_PATH + out_name
                    )
                else:
                    command = 'converter.exe -{0} -{1} all {2} -dir {3}'.format(
                        input_format,
                        output_format,
                        root + os.sep + file_path,
                        OUTPUT_PATH + out_name
                    )
                if os.system(command) == 0:
                    print(command, file=log_file)
                else:
                    print(command)
                    print('Error!!! %s not converted' % file_path, file=log_file)

    total_time = time.time() - start_time
    print('TIME: {}\n'.format(total_time), file=log_file)
    timer.configure(text='Time: {0:.3}'.format(total_time))


def ogf_object(event):
    run_command('ogf', 'object')


def ogf_bones(event):
    run_command('ogf', 'bones')


def ogf_skls(event):
    run_command('ogf', 'skls')


def ogf_skl(event):
    run_command('ogf', 'skl', all_option=True)


def omf_skls(event):
    run_command('omf', 'skls')


def omf_skl(event):
    run_command('omf', 'skl', all_option=True)


def dm_object(event):
    run_command('dm', 'object')


log_file = open(r'batch_converter.log', 'w')

# constants
BACKGROUND_COLOR = '#808080'
BUTTON_COLOR = '#A0A0A0'
ACTIVE_BUTTON_COLOR = '#B3B3B3'
BUTTON_WIDTH = 13
BUTTON_HEIGHT = 1
BUTTON_FONT = ('Font', 10, 'bold')
LABEL_FONT = ('Font', 8, 'bold')
BUTTON_1_TEXT = '{: <4}-> {: <6}'.format('ogf', 'object')
BUTTON_2_TEXT = '{: <4}-> {: <6}'.format('ogf', 'bones')
BUTTON_3_TEXT = '{: <4}-> {: <6}'.format('ogf', 'skls')
BUTTON_4_TEXT = '{: <4}-> {: <6}'.format('ogf', 'skl')
BUTTON_5_TEXT = '{: <4}-> {: <6}'.format('omf', 'skls')
BUTTON_6_TEXT = '{: <4}-> {: <6}'.format('omf', 'skl')
BUTTON_7_TEXT = '{: <4}-> {: <6}'.format('dm', 'object')

# main window
root = tkinter.Tk()
root.resizable(height=False, width=False)
root.minsize(width=240, height=320)
root.maxsize(width=240, height=320)
root.title('Batch Converter')
root['bg'] = BACKGROUND_COLOR
x = (root.winfo_screenwidth()) / 2
y = (root.winfo_screenheight()) / 2
root.geometry('+%d+%d' % (x - 120, y - 200))

frame = tkinter.Frame(root, bg=BACKGROUND_COLOR, width=240, height=320)

# buttons
ogf_object_button = tkinter.Button(
    frame, text=BUTTON_1_TEXT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
    bg=BUTTON_COLOR, activebackground=ACTIVE_BUTTON_COLOR, font=BUTTON_FONT
)
ogf_bones_button = tkinter.Button(
    frame, text=BUTTON_2_TEXT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
    bg=BUTTON_COLOR, activebackground=ACTIVE_BUTTON_COLOR, font=BUTTON_FONT
)
ogf_skls_button = tkinter.Button(
    frame, text=BUTTON_3_TEXT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
    bg=BUTTON_COLOR, activebackground=ACTIVE_BUTTON_COLOR, font=BUTTON_FONT
)
ogf_skl_button = tkinter.Button(
    frame, text=BUTTON_4_TEXT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
    bg=BUTTON_COLOR, activebackground=ACTIVE_BUTTON_COLOR, font=BUTTON_FONT
)
omf_skls_button = tkinter.Button(
    frame, text=BUTTON_5_TEXT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
    bg=BUTTON_COLOR, activebackground=ACTIVE_BUTTON_COLOR, font=BUTTON_FONT
)
omf_skl_button = tkinter.Button(
    frame, text=BUTTON_6_TEXT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
    bg=BUTTON_COLOR, activebackground=ACTIVE_BUTTON_COLOR, font=BUTTON_FONT
)
dm_object_button = tkinter.Button(
    frame, text=BUTTON_7_TEXT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
    bg=BUTTON_COLOR, activebackground=ACTIVE_BUTTON_COLOR, font=BUTTON_FONT
)

# labels
ver = tkinter.Label(frame, text='version 0.0.5', font=LABEL_FONT, bg=BACKGROUND_COLOR)
date = tkinter.Label(frame, text='14.06.2019', font=LABEL_FONT, bg=BACKGROUND_COLOR)
timer = tkinter.Label(frame, text='', font=LABEL_FONT, bg=BACKGROUND_COLOR)

# grid
frame.grid(row=0,  column=0, pady=42)
ogf_object_button.grid(row=4,  column=1, padx=64)
ogf_bones_button.grid(row=5,  column=1, padx=64)
ogf_skls_button.grid(row=6,  column=1, padx=64)
ogf_skl_button.grid(row=7,  column=1, padx=64)
omf_skls_button.grid(row=8,  column=1, padx=64)
omf_skl_button.grid(row=9,  column=1, padx=64)
dm_object_button.grid(row=10, column=1, padx=64)
timer.grid(row=11, column=1, padx=64, pady=8)
ver.grid(row=12, column=1, padx=64)
date.grid(row=13, column=1, padx=64)

# bind
LBM = '<Button-1>'
ogf_object_button.bind(LBM, ogf_object)
ogf_bones_button.bind(LBM, ogf_bones)
ogf_skls_button.bind(LBM, ogf_skls)
ogf_skl_button.bind(LBM, ogf_skl)
omf_skls_button.bind(LBM, omf_skls)
omf_skl_button.bind(LBM, omf_skl)
dm_object_button.bind(LBM, dm_object)

root.mainloop()
log_file.close()
