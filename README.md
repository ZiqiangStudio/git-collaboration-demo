# 技术中心 Git & GitHub 协作开发演示仓库

本仓库作为自强技术中心 **Git / GitHub 协作开发规范** 的实操演示载体。包含了 GitHub 生态中常见的协作功能样本，供团队成员直观体验和参考。

---

## 演示功能速览

1. **Issue 模板表单（GitHub Issue Forms）**
   - 缺陷反馈模版：`.github/ISSUE_TEMPLATE/bug_report.yml`
   - 功能需求模版：`.github/ISSUE_TEMPLATE/feature_request.yml`
2. **规范化 PR 模板（Pull Request Template）**
   - 变更背景、检查清单、关联 Issue 与自测截图：`.github/pull_request_template.md`
3. **自动化 CI 流水线（GitHub Actions）**
   - PR 标题规范校验（Conventional Commits 正则）：`.github/workflows/ci.yml`
   - 自动静态代码检查（Ruff）与单元测试（Pytest）
4. **Stacked PR 进阶演练（堆叠式 PR）**
   - 展示底层基线分支到上层增量分支的层级依赖与渐进式评审体验。
5. **Draft PR 草稿模式**
   - 标识进行中（WIP）状态，防止未完成代码被误合并。

---

## 本地快速开始

```bash
# 1. 克隆代码
git clone https://github.com/ZiqiangStudio/git-collaboration-demo.git
cd git-collaboration-demo

# 2. 安装 uv 依赖
uv venv
uv pip install -r pyproject.toml pytest ruff

# 3. 运行本地检查与测试
uv run ruff check .
uv run pytest
```
