import os, time, tkinter
from tkinter import filedialog

from xray import xray_ltx


VERSION = (0, 0, 7)


def run_command(input_format, output_format, all_option=False):
    # save settings
    input_dir = input_path_ent.get()
    output_dir = output_path_ent.get()
    settings_text = "[default_settings]\n"
    settings_text += 'input_dir = "{}"\n'.format(input_dir)
    settings_text += 'output_dir = "{}"\n'.format(output_dir)
    with open(settings_file_name, 'w', encoding='utf-8') as file:
        file.write(settings_text)

    mode = '{}->{}'.format(input_format.upper(), output_format.upper())
    log_text = ''
    mode_text = 'Run {} Converter\n'.format(mode)
    log_text += mode_text
    start_time = time.time()
    input_path = input_path_ent.get()
    input_path = input_path.replace('/', os.sep)
    output_path = output_path_ent.get()
    output_path = output_path.replace('/', os.sep)
    if not os.access(input_path, os.F_OK):
        timer.configure(text='Input folder does not exist!')
        return
    if not os.access(output_path, os.F_OK):
        os.makedirs(output_path)

    for root_folder, dirs, files in os.walk(input_path):
        for file_path in files:
            ext = file_path.split(os.extsep)[-1]
            out_name = os.path.join(
                root_folder[len(input_path): ],
                file_path[0 : -(len(ext) + 1)]
            )
            if ext == input_format:
                if not all_option:
                    command = 'converter.exe -{0} -{1} "{2}" -out "{3}.{1}"'.format(
                        input_format,
                        output_format,
                        os.path.join(root_folder, file_path),
                        os.path.join(output_path, out_name)
                    )
                else:
                    out_dir = os.path.join(output_path, out_name)
                    if not os.path.exists(out_dir):
                        os.makedirs(out_dir)
                    command = 'converter.exe -{0} -{1} all "{2}" -dir "{3}"'.format(
                        input_format,
                        output_format,
                        os.path.join(root_folder, file_path),
                        out_dir
                    )
                relative_dir = root_folder[len(input_path) : ]
                relative_path = os.path.join(relative_dir, file_path)
                final_command = 'echo off\n' + command
                if os.system(final_command) == 0:
                    print(relative_path)
                    log_text += command + '\n'
                else:
                    print('ERROR:', relative_path)
                    log_text += command + '\n'
                    log_text += 'Error!!! %s not converted\n' % file_path

    total_time = time.time() - start_time
    log_text += 'TIME: {}\n\n'.format(total_time)
    with open(log_path, 'a') as log_file:
        log_file.write(log_text)
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


def set_input():
    dir_path = filedialog.askdirectory()
    if dir_path:
        dir_path = dir_path.replace('/', os.sep) + os.sep
        module_dir = os.path.dirname(__file__) + os.sep
        if dir_path.startswith(module_dir):
            dir_path = dir_path[len(module_dir) : ]
        input_path_ent.delete(0, last=tkinter.END)
        input_path_ent.insert(0, dir_path)


def set_output():
    dir_path = filedialog.askdirectory()
    if dir_path:
        dir_path = dir_path.replace('/', os.sep) + os.sep
        module_dir = os.path.dirname(__file__) + os.sep
        if dir_path.startswith(module_dir):
            dir_path = dir_path[len(module_dir) : ]
        output_path_ent.delete(0, last=tkinter.END)
        output_path_ent.insert(0, dir_path)


# clear log file
log_path = 'stalker_batch_converter.log'
log_file = open(log_path, 'w')
log_file.close()

# constants
BACKGROUND_COLOR = '#808080'
BUTTON_COLOR = '#A0A0A0'
ACTIVE_BUTTON_COLOR = '#B3B3B3'
BUTTON_WIDTH = 13
BUTTON_HEIGHT = 1
BUTTON_FONT = ('Font', 10, 'bold')
ENTRY_FONT = ('Font', 7, 'bold')
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
root.minsize(width=320, height=320)
root.maxsize(width=320, height=320)
root.title('Batch Converter v{}.{}.{}'.format(*VERSION))
root['bg'] = BACKGROUND_COLOR
x = (root.winfo_screenwidth()) / 2
y = (root.winfo_screenheight()) / 2
root.geometry('+%d+%d' % (x - 320 / 2, y - 200))

frame = tkinter.Frame(root, bg=BACKGROUND_COLOR, width=320, height=320)
frame_paths = tkinter.Frame(frame, bg=BACKGROUND_COLOR)

# entry
input_path_ent = tkinter.Entry(frame_paths, width=50, font=ENTRY_FONT, bg=BUTTON_COLOR)
output_path_ent = tkinter.Entry(frame_paths, width=50, font=ENTRY_FONT, bg=BUTTON_COLOR)

# buttons
set_input_button = tkinter.Button(
    frame_paths, text='Input', width=7, height=BUTTON_HEIGHT,
    bg=BUTTON_COLOR, activebackground=ACTIVE_BUTTON_COLOR, font=ENTRY_FONT,
    command=set_input
)
set_output_button = tkinter.Button(
    frame_paths, text='Output', width=7, height=BUTTON_HEIGHT,
    bg=BUTTON_COLOR, activebackground=ACTIVE_BUTTON_COLOR, font=ENTRY_FONT,
    command=set_output
)

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
ver = tkinter.Label(frame, text='version {}.{}.{}'.format(*VERSION), font=LABEL_FONT, bg=BACKGROUND_COLOR)
date = tkinter.Label(frame, text='2021.07.17', font=LABEL_FONT, bg=BACKGROUND_COLOR)
timer = tkinter.Label(frame, text='', font=LABEL_FONT, bg=BACKGROUND_COLOR)

# grid
frame.grid(row=0,  column=0, pady=0)
frame_paths.grid(row=0,  column=1, pady=10)
input_path_ent.grid(row=0,  column=0, padx=5)
set_input_button.grid(row=0,  column=1, padx=0)
output_path_ent.grid(row=1,  column=0, padx=0)
set_output_button.grid(row=1,  column=1, padx=0)
ogf_object_button.grid(row=4,  column=1, padx=64)
ogf_bones_button.grid(row=5,  column=1, padx=64)
ogf_skls_button.grid(row=6,  column=1, padx=64)
ogf_skl_button.grid(row=7,  column=1, padx=64)
omf_skls_button.grid(row=8,  column=1, padx=64)
omf_skl_button.grid(row=9,  column=1, padx=64)
dm_object_button.grid(row=10, column=1, padx=64)
timer.grid(row=11, column=1, padx=64, pady=0)
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

if not input_path_ent.get():
    INPUT_PATH = 'input' + os.sep
    input_path_ent.delete(0, tkinter.END)
    input_path_ent.insert(0, INPUT_PATH)
else:
    INPUT_PATH = input_path_ent.get()

if not output_path_ent.get():
    OUTPUT_PATH = 'output' + os.sep
    output_path_ent.delete(0, tkinter.END)
    output_path_ent.insert(0, OUTPUT_PATH)
else:
    OUTPUT_PATH = output_path_ent.get()

# settings
settings_file_name = 'stalker_batch_converter.ini'
if os.path.exists(settings_file_name):
    settings = xray_ltx.StalkerLtxParser(settings_file_name)
    default_settings = settings.sections.get('default_settings', None)
    if default_settings:
        input_path_ent.delete(0, last=tkinter.END)
        input_path_ent.insert(0, default_settings.params['input_dir'])

        output_path_ent.delete(0, last=tkinter.END)
        output_path_ent.insert(0, default_settings.params['output_dir'])

root.mainloop()
