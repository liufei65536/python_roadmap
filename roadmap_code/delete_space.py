str=r"""
a. 如 果 X . C; 只 含 有 t — 1 个 关 键 字 ， 但 是 它 的 一 个 相 邻 的 兄 弟 至 少 包 含 t个 关 键 字 ， 则 将 x
中 的 某 一 个 关 键 字 降 至 X , C; 中 ， 将 X , C; 的 相 邻 左 兄 弟 或 右 兄 弟 的 一 个 关 键 字 升 至 x , 将 该 兄 弟
中 相 应 的 孩 子 指 针 移 到 X . C; 中 ， 这 样 就 使 得 X . C; 增 加 了 一 个 额 外 的 关 键 字 。
b. 如 果 X . C; 以 及 X , C; 的 所 有 相 邻 兄 弟 都 只 包 含 t — 1 个 关 键 字 ， 则 将 X , C; 与 一 个 兄 弟 合 并 ，
即 将 x 的 一 个 关 键 字 移 至 新 合 并 的 结 点 ， 使 之 成 为 该 结 点 的 中 间 关 键 字 。
"""
new_str = ""
for x in str:
    if  x not in [' ', '\n']:
        new_str += x
print(new_str)