<!-- omit in toc -->
# 目次
- [numpy](#numpy)
  - [線形代数関連](#線形代数関連)
    - [単位行列生成 np.eye()、np.indentity()](#単位行列生成-npeyenpindentity)
- [あとがき](#あとがき)

[Top]: #目次

# numpy
pythonにおける数値計算ライブラリ
基本的な行列計算は大体numpyがサポートしており、他言語に比べて処理速度が遅いpythonにおいて効率的に演算が行える
numpyをベースとした書き方ができるかどうかで、処理速度がかなり変わってくるのでpythonを使用する上できちんと理解する必要がある


## 線形代数関連
### 単位行列生成 np.eye()、np.indentity()
行数を指定することで、そのサイズの単位行列を生成できる。**eye()** の方は正方行列以外の形にでも生成が可能
速度面に大した差はないらしいので、基本的に**eye()** の方を使えば問題ない
```python
import numpy as np

eye = np.eye(5)
identity = np.identity(5)
```

# あとがき

[Topに戻る][Top]
