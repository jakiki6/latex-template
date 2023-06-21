with open("data.csv", "r") as f:
    lines = f.read().split("\n")

# description line
desc = lines.pop(0).split("; ")

# process
data = []
for line in lines:
    if line.strip() == "":
        continue

    line = line.replace(" ", "").replace(",", ".").split(";")[1:]
    try:
        data.append([eval(piece) for piece in line])
    except:
        pass

for i in range(0, 4):
    content = "\\begin{tikzpicture}\n\\begin{axis}[title={" + desc[2+i] + "},xlabel={Zeit (in s)},ylabel={" + desc[2+i] + "},grid style=dashed]\n\\addplot[color=blue,mark=square]\n"

    content += "coordinates {"
    for j in range(0, len(data)):
        content += f"({data[j][0]},{data[j][1+i]})"
    content += "};\n"
    content += "\end{axis}\n\end{tikzpicture}\n"

    print(content)
