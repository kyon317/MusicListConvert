import re


def convert(name):
    # Read the file
    with open(name, 'r', encoding='utf-8') as f:
        content = f.read()

    # Perform the replacements and regex cleanup
    modified_content = content.replace("歌曲名：", "") \
        .replace("，歌手名：", " - ")

    modified_content = re.sub(r'，专辑名：.*', "", modified_content)

    # Write the modified content back to the file
    with open(name, 'w', encoding='utf-8') as f:
        f.write(modified_content)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert('list.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
