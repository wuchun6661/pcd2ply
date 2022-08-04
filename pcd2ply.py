import re
import sys


def pcd2ply(data):
    p1 = re.compile(r'POINTS[\s](\d+)')
    p2 = re.compile(r'^([-\d.]+)\s([-\d.]+)\s([-\d.]+)\s([\d]+)', re.M)
    num_pcd = p1.findall(data)[0]
    content = p2.findall(data)
    num_avail = len(content)
    print(f"PCD文件总点数：{num_pcd}  |  有效点数：{num_avail}")
    # print(type(content), type(content[0]), type(content[0][0]))
    return [num_avail, content]


def write_ply(num, ply_content, outpath):
    ply_header = f'''ply
format ascii 1.0
comment PCL generated
element vertex {num}
property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue
element camera 1
property float view_px
property float view_py
property float view_pz
property float x_axisx
property float x_axisy
property float x_axisz
property float y_axisx
property float y_axisy
property float y_axisz
property float z_axisx
property float z_axisy
property float z_axisz
property float focal
property float scalex
property float scaley
property float centerx
property float centery
property int viewportx
property int viewporty
property float k1
property float k2
end_header\n'''
    ply_end = f"0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 {num} 1 0 0"
    body = ""
    for i, one in enumerate(ply_content):
        rgb = int(one[3])
        r = str(int(rgb/256**2 % 256))
        g = str(int(rgb/256 % 256))
        b = str(int(rgb % 256))
        body += f"{one[0]} {one[1]} {one[2]} {r} {g} {b}\n"
        # body += f"{one[0]} {one[1]} {one[2]}\n"
        # if i >= num-1:
        #     break
    result = ply_header + body + ply_end
    with open(outpath, 'w+') as f:
        f.write(result)
    # print(result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("你的输入参数不对，请按照以下格式[xxxx.py] [input.pcd] [output.ply]")
        sys.exit(1)
    input = sys.argv[1]
    output = sys.argv[2]
    with open(input, "r", encoding='utf-8') as f:
        content = f.read()
        print(f"打开文件{input}成功")
    num, ply_content = pcd2ply(content)
    print(f"完成{input}内容筛选")
    write_ply(num, ply_content, output)
    print(f"完成{output}写入")

