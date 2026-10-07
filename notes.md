## 2026-10-07 | ReAct 首个闭环跑通

**产出**：main.py 一条命令跑通 ReAct agent，模型自主搜索并回答"英伟达最新GPU"

**今天踩的坑（按值钱程度排序）**：
1. 版本漂移：pip 默认装 serpapi 1.1.2，旧类名已删；降级 1.0.5 签名仍不符 → 终局方案：requests 直连 REST API，不依赖第三方 SDK
2. .env 不会自动生效：os.getenv 读进程变量，谁用谁 load_dotenv
3. 文档里 `# (这段逻辑在...)` 是位置说明不是代码，照抄会结构错乱
4. 排错心法：先分清"范式跑通"还是"工具有bug"，别把工具报错当成范式失败

**待办**：Plan-and-Solve 范式（4.2 后半）；requirements 锁版本