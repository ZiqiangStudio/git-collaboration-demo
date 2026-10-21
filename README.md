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
6. **环境变量与机密管理规范（gh secret set -f .env）**
   - 遵循 `.env.example` 契约声明与代码优雅降级，使用 GitHub CLI 原生命令一键全量同步 Secrets。

---

## 本地快速开始

```bash
# 1. 克隆代码
git clone https://github.com/ZiqiangStudio/git-collaboration-demo.git
cd git-collaboration-demo

# 2. 准备本地环境变量（从模板复制）
cp .env.example .env

# 3. 安装 uv 依赖
uv venv
uv pip install -r pyproject.toml pytest ruff

# 4. 运行本地检查与测试
uv run ruff check .
uv run pytest
```

---

## 环境变量与 Secrets 同步规范

团队统一遵循以下极简协作闭环：

### 1. 代码默认值兜底（从源头杜绝崩溃）
- 代码中读取环境变量必须提供合理的默认值（`default`）或平滑降级（如未配置 OSS 时自动降级为本地存储）：
  ```python
  # 推荐写法：漏填也能安全启动
  SECRET_KEY = config("SECRET_KEY", default="django-insecure-demo-secret-key")
  ```

### 2. 模板即契约（.env.example）
- 任何人在代码中新增或调整了环境变量，必须同步在 `.env.example` 中登记说明与示例值。

### 3. GitHub CLI 原生极简同步（推荐团队统一方式）
- 杜绝在 GitHub 网页控制台逐条手动复制粘贴，容易遗漏且效率低。
- 在本地准备好 `.env` 配置文件后，直接运行 GitHub CLI 原生一行命令：
  ```bash
  # 一键将本地整份 .env 文件全量推送到仓库 Secrets
  gh secret set -f .env

  # 若部署在 production 环境，同步至指定环境
  gh secret set -f .env --env production
  ```

### 4. PR 审查闭环机制
- Reviewer 在审阅 PR 时，只要看到 Files Changed 中包含 `.env.example` 变动，在评论区顺手确认一句：“新增变量是否已通过 `gh secret set -f .env` 同步？”确保上线前配置闭环。
