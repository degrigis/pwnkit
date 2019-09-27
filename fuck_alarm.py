import os
import sys
import shutil

# FUN FACT: sed -i 's/sleep/isinf/g' <binary_name>
def patch_binary(binary_path):

    def patch(data):
        p = data
        p = p.replace(b'alarm', b'isinf')
        # data = data.replace(b'close', b'isnan')  # for binaries that close stdout
        return data

    with open(binary_path, 'rb') as f:
        original = f.read()

    patched = patch(original)

    with open(binary_path, 'wb') as f_out:
        f_out.write(patched)

    os.chmod(binary_path, 0o555)

if __name__ == "__main__":
    if sys.argc != 2:
        print("Usage: python fuck_alarm.py <binary_name>")
        sys.exit(0)

    binary_path = sys.argv[1]

    if os.path.isfile(binary_path):
        shutil.copyfile(binary_path, binary_path + ".bak")
        patch_binary(binary_path)
    else:
        print("File {} not found".format(binary_path))
