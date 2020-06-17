这是一个简单的使用 Cython 包装 C++ 库的例子，从 Cython 的使用手册中修改而来。

这份代码比较简单，`rectangle` 目录下为 C++ 代码，里面写有一个简单的 `CMakeLists.txt`，编译之后可以得到 `librectangle.so`。按照惯例，配置，然后编译即可：

```bash
# 克隆仓库代码并切换到目录
git clone https://github.com/hubutui/cython-cpp-example.git
cd cython-cpp-example
# 后面的操作我们都假定你在源码根目录下
cmake -B rectangle/build -S rectangle
cmake --build rectangle/build
```

构建成功之后，我们已经就可以在 `rectangle/build` 目录下看到一个 `librectangle.so` 文件，也就是我们编译好的动态链接库了。

下面开始编译 python 代码：

```bash
python setup.py build
```

编译完毕之后，应该会得到文件 `build/lib.linux-x86_64-3.8/rect.cpython-38-x86_64-linux-gnu.so`，具体目录跟你使用的系统以及 python 版本有所不同。然后我们就可以使用 python 来测试一下了。

注意一下我在 `setup.py` 文件中设置了 `library_dirs`，`include_dirs` 和 `runtime_library_dirs`，前两者是设置了 `librectangle` 库的查找目录，后者是设置了运行时的 `librectangle` 库查找目录，可以对应到 `python setup.py build_ext` 命令的 `--library-dirs`，`--include-dirs` 和 `--rpath` 这几个选项。

为了能让 python 查找到 cython 编译出来动态链接库，我们需要设置 `PYTHONPATH`，这个值可以在启动 python 的时候通过环境变量 `PYTHONPATH` 指定，也可以在启动 python 之后使用 `sys` 模块来指定。

```bash
# 启动 python 的时候指定 PYTHONPATH
PYTHONPATH=build/lib.linux-x86_64-3.8 python
import rect
```

或者在 python 中使用 `sys` 来设置 `PYTHONPATH`：

```python
import sys
sys.path.append('build/lib.linux-x86_64-3.8')
import rect
```

参考：
1. http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html
2. http://docs.cython.org/en/latest/src/tutorial/clibraries.html