from pathlib import Path

path = Path('Try this item.txt')
contents = path.read_text()
print(contents)