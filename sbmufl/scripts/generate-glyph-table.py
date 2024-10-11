#!/usr/bin/env python3

file = open("../../sources/namelist.txt")

print(
    """<style>
            @font-face {
                font-family: Almouzios;
                src: url('../../../Almouzios.otf');
            }

            .neumes {
                font-family: Almouzios;
                font-size: 100pt;
            }

            .code-point {
                font-weight: bold;
            }

            .glyph-name {
                
            }

            table {
                border-collapse: collapse;
            }

            td {
                padding: 3px 20px;
                border: 1px gray solid;
            }

            td .neumes {
                display: flex;
                justify-content: center;
            }
</style>"""
)

print("<table>")

line = file.readline()
while line:
    line = line.rstrip()
    words = line.split(" ")
    glyph_name = words[1]
    code_point = words[0].removeprefix("0x")
    html = f"""<tr>
    <td>
        <span class="neumes">&#x{code_point};</span>
    </td>
    <td>
        <div class="code-point">
            U+{code_point.upper()}
        </div>
        <div class="glyph-name">
            {glyph_name}
        </div>
    </td>
</tr>"""
    print(html)
    line = file.readline()

print("</table>")
print("</body></html>")

file.close()
