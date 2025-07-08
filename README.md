# Unicode 数学符号输入

这是一个基于 [RIME](https://rime.im) 输入法引擎的输入方案，允许你用类似 LaTeX 乃至更直观的命令输入 Unicode 数学符号。

## 使用场景

如果你想在聊天或评论区输入数学公式，就会发现许多软件并不支持 LaTeX。直接输入 LaTeX 命令或用 ASCII 替代虽然也可以传达给训练有素的读者，但是并不直观。好在 Unicode 已经纳入许多数学符号，只需要有一个输入法，你就可以优雅地将公式直接输入为文本。

另一方面，如果你真的使用 LaTeX，就会发现源码中的命令不太可读，特别是数学公式。如果能直接输入 Unicode 数学符号并使 LaTeX 能够解析，LaTeX 源码的可读性可以大大提升。本项目可以负责输入部分，让 LaTeX 能够解析你输入的 Unicode 符号可以参考 [这里](#latex-unicode-数学符号解析)。

## 用法简介

命令示例：
- 用 `\exists` 输入 `∃`
- 用 `\_1` 输入 `₁`
- 用 `\==>` 输入 `⟹`

在不键入 `\` 时，此输入法可直接当作英文输入法，可无缝衔接编程或英文论文写作。键入 `\\` 以输入单个 `\`。

为方便不同使用场景和习惯，此项目除命令以 `\` 开始的版本外，另提供命令以 `@` 或 `;` 开始的两个版本。三个版本的命令除开始的符号外完全一致，如 `;` 版本上面的命令分别是 `;exists`、`;_1` 和 `;==>`。类似地，键入 `@@` 或 `;;` 以输入单个 `@` 或 `;`。

命令列表最初由 [Lean4 VSCode 扩展](https://github.com/leanprover/vscode-lean4/blob/master/lean4-unicode-input/src/abbreviations.json) 改编而来。

## 安装

1. 在 [RIME 的网站](https://rime.im) 安装合适的 RIME 输入法。
   
   如 Windows 用户可安装小狼毫，视需求安装自带的输入方案。
2. 将本项目的 6 个 YAML 文件放在 [用户文件夹](https://github.com/rime/home/wiki/UserData) 下。
   
   以小狼毫为例，切换到小狼毫后右击输入法工具栏中的“中”图标，弹出的菜单可快速到达用户文件夹。
3. 在 default.custom.yaml 或输入法图形界面中选中“Unicode 数学符号”输入方案（或 `@`、`;` 的版本）。
   
   以小狼毫为例，可在上一步的菜单中找到“输入法设定”，在弹出的窗口中勾选这些输入方案。

4. 开始试用！注意如果你还选用了其他 RIME 输入方案，可能需要先切换到 Unicode 数学符号输入的某个版本。

## 升级

1. 用新版本的 6 个 YAML 文件覆盖旧版本。
2. [重新部署](https://github.com/rime/home/wiki/CustomizationGuide#%E9%87%8D%E6%96%B0%E4%BD%88%E7%BD%B2%E7%9A%84%E6%93%8D%E4%BD%9C%E6%96%B9%E6%B3%95) 输入法数据。
   
   以小狼毫为例，重新部署仍可以在上述菜单中找到。

## 命令检索

可自行参阅各 .dict.yaml 文件，或用以生成三个版本的 [source.md](./source.md) 文件。通常情况下，命令与 Lean4 VSCode 扩展或 LaTeX `unicode-math` 宏包对应。

## 自定义命令

在用户文件夹中的 [unicode_math.dict.yaml](./unicode_math.dict.yaml) 文件末尾新增一行，输入以 <kbd>Tab</kbd> 隔开的输入结果和命令即可。保存后，[重新部署](https://github.com/rime/home/wiki/CustomizationGuide#%E9%87%8D%E6%96%B0%E4%BD%88%E7%BD%B2%E7%9A%84%E6%93%8D%E4%BD%9C%E6%96%B9%E6%B3%95) 输入法数据即可。

命令以 `@` 开始和 `;` 的版本则对应修改 [unicode_math_at.dict.yaml](./unicode_math_at.dict.yaml) 或 [unicode_math_semi.dict.yaml](./unicode_math_semi.dict.yaml)。

※注意：
- `\` 开始的版本添加的命令必须以反斜杠 `\` 开始。`@` 和 `;` 开始的版本类似。这是由 [unicode_math.schema.yaml](./unicode_math.schema.yaml) 等文件中 `speller.initials` 一项决定的。
- 不要以空格替换分隔输入结果和命令的 <kbd>Tab</kbd>。

如果想要一次修改三个版本，乃至向此项目提 Pull Request，可以修改 [source.md](./source.md)，并运行 [generate.py](./generate.py) 同时生成三份 .dict.yaml。

## LaTeX Unicode 数学符号解析

在 LaTeX 中有若干宏包可以支持将 Unicode 字符解析为对应的命令，如 `α` 解析为 `\alpha`。可以从下面两个宏包中二选一：
```LaTeX
\usepackage{unicode-math} % 仅支持 Unicode 引擎，如 XeLaTeX 或 LuaLaTeX
\usepackage{unicode-math-input} % 也支持 pdfLaTeX
```
特别地，两者均支持连续上下标。如 `x¹²ᵢⱼ` 可以解析成 `x^{12}_{ij}`。

### 扩充或修改符号解析

偶尔，输入的符号可能在上述宏包支持范围之外，或者需要调整某个符号对应的具体命令。对于 `unicode-math-input`，可以使用如下命令修改，详见宏包文档：
```LaTeX
\umiDeclareMathChar{▷}{\vartriangleright} % 给出单个字符和替换的内容
```
有必要时甚至可以修改上下标字符（未在宏包文档中给出，慎用）：
```LaTeX
\ExplSyntaxOn
\umiDeclareMathChar{ˡ}{\__umi_superscript{\ell}} % 将所有 ˡ 从 l 上标修改为 ℓ 上标
\umiDeclareMathChar{ₗ}{\__umi_subscript{\ell}} % 将所有 ₗ 从 l 下标修改为 ℓ 下标
\ExplSyntaxOff
```

一般地，可以使用 `newunicodechar` 宏包：
```LaTeX
\usepackage{newunicodechar}
\newunicodechar{▷}{\vartriangleright} % 给出单个字符和替换的内容
```

## 开源许可

本项目与命令列表来源 Lean4 VSCode 扩展均遵循 [Apache 2.0](./LICENSE) 许可证。
