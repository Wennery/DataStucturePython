
class SqList:
    def __init__(self):
        self.initcapacity = 5  # 初始容量，固定为5
        self.capacity = self.initcapacity  # 当前容量，初始等于初始容量
        self.data = [None] * self.capacity  # 存储元素的列表（数据区）
        self.size = 0  # 当前元素数量（有效元素个数）

    def resize(self, new_capacity):
        """调整顺序表的容量（扩容或缩容）"""
        assert new_capacity >= 0  # 确保新容量非负
        old_data = self.data  # 保存旧数据引用
        self.data = [None] * new_capacity  # 创建新容量的数据区
        # 复制旧数据到新数据区（只复制有效元素）
        for i in range(self.size):
            self.data[i] = old_data[i]
        self.capacity = new_capacity  # 更新当前容量

    def CreateList(self, a):
        """根据传入的列表a创建顺序表（批量添加元素）"""
        for i in range(len(a)):
            # 若元素满了，先扩容为原来的2倍
            if self.size == self.capacity:
                self.resize(2 * self.capacity)
            self.data[self.size] = a[i]  # 元素添加到尾部
            self.size += 1  # 元素数量加1

    def Add(self, e):
        """在顺序表尾部添加单个元素e"""
        # 若容量不足，先扩容
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.data[self.size] = e  # 元素放入尾部
        self.size += 1  # 数量加1

    def GetSize(self):
        """返回顺序表中元素的数量"""
        return self.size

    def GetElem(self, i):
        """获取索引i处的元素（索引从0开始）"""
        assert i >= 0 and i < self.size  # 检查索引合法性
        return self.data[i]

    def __getitem__(self, i):
        """重载[]运算符，支持通过sq[i]访问元素"""
        assert i >= 0 and i < self.size  # 检查索引合法性
        return self.data[i]

    def __setitem__(self, i, x):
        """重载[]运算符，支持通过sq[i] = x修改元素"""
        assert i >= 0 and i < self.size  # 检查索引合法性
        self.data[i] = x

    def GetNo(self, e):
        """查找元素e的索引，找到返回索引，未找到返回-1"""
        for i in range(self.size):
            if self.data[i] == e:
                return i
        return -1

    def Insert(self, i, e):
        """在索引i处插入元素e（原i及之后元素后移）"""
        assert i >= 0 and i < self.size  # 检查插入位置合法性
        # 容量不足则扩容
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        # 元素从尾部到i依次后移，腾出位置
        for j in range(self.size, i, -1):
            self.data[j] = self.data[j - 1]
        self.data[i] = e  # 插入元素
        self.size += 1  # 数量加1

    def Delete(self, i):
        """删除索引i处的元素（原i之后元素前移），必要时缩容"""
        assert i >= 0 and i < self.size  # 检查删除位置合法性
        # 元素从i到尾部前一位依次前移，覆盖待删除元素
        for j in range(i, self.size-1):
            self.data[j] = self.data[j+1]
        self.size -= 1  # 数量减1
        # 若元素数量小于容量的1/4，缩容为原来的1/2（节省空间）
        if self.capacity > self.initcapacity and self.size <= self.capacity / 4:
            self.resize(self.capacity // 2)

    def display(self):
        """打印顺序表中所有元素（空格分隔）"""
        for i in range(self.size):
            print(self.data[i], end=' ')
        print()  # 换行

    def Delete(self, i, k):
        """删除索引i到i+k-1 处的元素（原i+k-1之后元素前移），必要时缩容"""
        assert i >= 0 and k >= 1 and i+k-1 < self.size  # 检查删除范围合法性
        # 元素从i+k-1到尾部前一位依次前移，覆盖待删除元素
        for j in range(i+k, self.size):
            self.data[j-k] = self.data[j]
        self.size -= k  # 数量减k
        # 若元素数量小于容量的1/4，缩容为原来的1/2（节省空间）
        if self.capacity > self.initcapacity and self.size <= self.capacity / 4:
            self.resize(self.capacity // 2)


def test_sqlist():
    # 1. 初始化顺序表
    sq = SqList()
    print("初始化顺序表后，大小为:", sq.GetSize())
    print("初始容量为:", sq.capacity)
    print()

    # 2. 创建列表
    data = [10, 20, 30, 40, 50]
    sq.CreateList(data)
    print("创建列表后的数据:")
    sq.display()
    print("当前大小:", sq.GetSize())
    print("当前容量:", sq.capacity)
    print()

    # 3. 添加元素（测试扩容）
    sq.Add(60)
    sq.Add(70)
    print("添加元素后的内容:")
    sq.display()
    print("添加后大小:", sq.GetSize())
    print("添加后容量(应自动扩容):", sq.capacity)
    print()

    # 4. 获取元素
    print("索引为2的元素:", sq.GetElem(2))
    print("使用[]访问索引3的元素:", sq[3])
    print()

    # 5. 修改元素
    sq[1] = 200
    print("修改索引1的元素后:")
    sq.display()
    print()

    # 6. 查找元素
    print("查找元素30的位置:", sq.GetNo(30))
    print("查找不存在元素99的位置:", sq.GetNo(99))
    print()

    # 7. 插入元素
    sq.Insert(2, 150)
    print("在索引2插入150后:")
    sq.display()
    print("插入后大小:", sq.GetSize())
    print()

    # 8. 删除元素（测试缩容）
    sq.Delete(0)  # 删除第一个元素
    sq.Delete(5)  # 删除索引5的元素
    print("删除元素后:")
    sq.display()
    print("删除后大小:", sq.GetSize())
    
    # 连续删除元素，触发缩容
    sq.Delete(0)
    sq.Delete(0)
    sq.Delete(0)
    sq.Delete(0)
    print("连续删除后:")
    sq.display()
    print("连续删除后大小:", sq.GetSize())
    print("连续删除后容量(应自动缩容):", sq.capacity)

if __name__ == "__main__":
    test_sqlist()
