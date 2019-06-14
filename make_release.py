from zipfile import ZipFile, ZIP_DEFLATED
from os import path, walk


version = (0, 0, 4)
with ZipFile('stalker_batch_converter_' + ('.'.join(map(str, version))) + '.zip', 'w') as z:
    z.write(
        'stalker_batch_converter.py',
        'stalker_batch_converter/stalker_batch_converter.py',
        compress_type=ZIP_DEFLATED
    )
    z.write(
        'converter.exe',
        'stalker_batch_converter/converter.exe',
        compress_type=ZIP_DEFLATED
    )
    z.write(
        'readme.txt',
        'stalker_batch_converter/readme.txt',
        compress_type=ZIP_DEFLATED
    )
