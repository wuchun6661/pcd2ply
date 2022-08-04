# 简介

1、该功能包，能在ascii编码下，将pcd转ply

2、先通过pcl库将pcd文件（binary）转pcd文件（ascii），然后通过pcd2ply.py将pcd转为ply

# Example

命令在run.sh文件里

```bash
#把pcd的编码方式：binary----->ascii
pcl_convert_pcd_ascii_binary r3live_binary.pcd r3live_ascii.pcd 0
#python将pcd(ascii)------->ply(ascii)
python3 pcd2ply.py r3live_ascii.pcd r3live_ascii.ply
```
