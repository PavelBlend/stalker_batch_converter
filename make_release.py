from zipfile import ZipFile, ZIP_DEFLATED
from os import path, walk


version = (0, 0, 8)
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
        'README.md',
        'stalker_batch_converter/README.md',
        compress_type=ZIP_DEFLATED
    )
    z.write(
        'xray\\__init__.py',
        'stalker_batch_converter/xray/__init__.py',
        compress_type=ZIP_DEFLATED
    )
    z.write(
        'xray\\lzhuf.py',
        'stalker_batch_converter/xray/lzhuf.py',
        compress_type=ZIP_DEFLATED
    )
    z.write(
        'xray\\xray_io.py',
        'stalker_batch_converter/xray/xray_io.py',
        compress_type=ZIP_DEFLATED
    )
    z.write(
        'xray\\xray_ltx.py',
        'stalker_batch_converter/xray/xray_ltx.py',
        compress_type=ZIP_DEFLATED
    )
input('Finish')
