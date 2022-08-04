#把pcd的编码方式：binary----->ascii
pcl_convert_pcd_ascii_binary r3live_binary.pcd r3live_ascii.pcd 0

#python将pcd(ascii)------->ply(ascii)
python3 pcd2ply.py r3live_ascii.pcd r3live_ascii.ply
