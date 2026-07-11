# Python 零基础学习记录

一个从零开始学 Python 的真实记录。每行代码都手写，每个概念都练到能独立写出才继续。

## 学习原则

- **学会 > 了解**：不看资料，从空白文件能写出来才算学会
- **一次一个概念**：不赶进度，练熟再走
- **每行都有注释**：用自己的话解释每行代码做了什么
- **不怕报错**：报错是最好的老师

## 学习轨迹

### Day 01 · 2026-07-06 — 文件操作入门

> 第一份代码：读取同目录下的文件，逐行打印

`day01-file-io/`

| 文件 | 内容 |
|------|------|
| `26-7-6.py` | 完整注释版：`import os` → `with open` → `for line` → `strip()` |
| `ips.txt` | 测试用文件（放一个 IP 地址） |

**首次接触的概念：**
`import` `__file__` `os.path.dirname` `os.path.join` `os.path.exists` `if/else` `with open` `for line` `strip()`

---

### Day 02 · 2026-07-07 — 复习巩固 + 列表 + 字典

> 上午复习文件操作，下午列表入门，傍晚组合运用，晚上字典 + 编码

`day02-list/`

| 文件 | 内容 |
|------|------|
| `26-7-7.py` | 复习：换场景独立写出（ips.txt → hosts.txt） |
| `26-7-7（2）.py` | 热身：隔半天再写一次 |
| `26-7-7(3).py` | 列表探索：`[]` 创建、`[0]` 下标、`[4]` 访问 |
| `26-7-7(4).py` | UnicodeDecodeError → `encoding='utf-8'` 修复；下标取首尾行 |
| `26-7-7(5).py` | 字典入门：`enumerate()` + `lyrics_dict[i] = line.strip()` |
| `config.txt` | 测试用歌词文件（46 行中文） |

**新接触的概念：**
`list` `[ ]` `下标访问` `.append()` `len()` `dict` `{ }` `enumerate()` `f.readlines()` `encoding='utf-8'`

**踩坑记录：**
- `open()` 在 Windows 上默认用 GBK 读，中文文件报 `UnicodeDecodeError` → 显式指定 `encoding='utf-8'`
- `f` 是文件对象（file object），不是函数
- 字典用 `[键]` 取值和赋值，列表用 `[下标]`；字典没有 `.append()`

---

## 环境

- Python 3.12
- VS Code
- Windows 11

---

### Day 06 · 2026-07-11 — 字符串切割 + 全链路整合

> 状态恢复日：不学新概念，用综合练习把前五天的知识点串成一条线

`2026-07-11/`

| 文件 | 内容 |
|------|------|
| `1.py` | 文件读取 + split 切割 + for 缩进陷阱修复 + 逐行中文注释 |
| `2.py` | 完整链路：文件→split→字典→列表→函数→f-string 输出 |
| `scores.txt` | 测试数据（虚构角色名） |

**新概念：** `split()` `split(":")` `f-string` `int()`

**复习巩固：** `import os` `dirname` `join` `exists` `with open` `for line` `strip` `list` `append` `dict` `def` `return` `if/elif/else`

**踩坑：** 嵌套 for 导致数据重复——外层每读一行，内层就重印全部已读数据

---

## 为什么会有这个仓库

学编程最怕「看得懂，写不出」。这里记录的是「从写不出到写得出的过程」——不是完美的成品代码，而是带有大量注释、踩过坑、一步步迭代的真实学习痕迹。希望对同样零基础的人有帮助。
