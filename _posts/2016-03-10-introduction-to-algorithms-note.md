---
published: true
title: 算法导论第二版算法摘录及重点（未完成）
layout: post
author: linnet8989
category: algorithms
tags:
- algorithm
- note
---

# 第一部分 基础知识

## 第2章 算法入门

### 插入排序（ O(n<sup>2</sup>) ）

~~~
for j ← 2 to length[A]
	key ← A[j]
		i ← j-1
		while i>0 and A[i]>key
			A[i+1] ← A[i]
			i ← i-1
		A[i+1] ← key
~~~

插入排序使用的是增量(incremental)方法：在排好子数组A[1..j-1]后，将元素A[j]插入，形成排好序的子数组A[1..j]。

### 分治法与递归——合并排序（O(nlgn)）

#### 分治法
有很多算法在结构上是递归的：为了解决一个给定的问题，算法要一次或多次地递归调用其自身来解决相关的子问题。这些算法通常采用分治策略。

分治模式在每一层递归上都有三个步骤。

~~~
分解(Divide)：将原问题分解成一系列子问题
解决(Conquer)：递归地解各子问题。若子问题足够小，则直接求解
合并(Combine)：将子问题的结果合并成原问题的解
~~~

#### 合并的伪代码

~~~
MERGE(A, p, q, r)
	n1 ← q-p+1
	n2 ← r-q
	create arrays L[1..n1+1] and R[1..n2+1]
	for i ← 1 to n1
		L[i] ← A[p+i-1]
	for j ← 1 to n2
		R[j] ← A[q+j]
	L[n1+1] ← ∞
	R[n2+1] ← ∞
	i ← 1
	j ← 1
	for k ← p to r
		if L[i] ≤ R[j]
			then A[k] ← L[i]
			     i ← i+1
			else A[k] ← R[j]
			     j ← j+1
~~~

#### 排序的算法（O(nlgn)）

~~~
MERCGE-SORT(A, p, r)
	if p < r
		then q ← [(p+r)/2]
		     MERGE-SORT(A, p, q)
		     MERGE-SORT(A, q+1, r)
		     MERGE(A, p, q, r)
~~~

合并排序算法完全依照了分治模式，其操作如下：

~~~
分解：将n个元素分成各含n/2个元素的子序列
解决：用合并排序法对两个子序列递归地排序
合并：合并两个已排序的子序列以得到排序结果
~~~

在对子序列排序时，其长度为1时递归结束。单个元素被视为是已排好序的。

#### 附：冒泡排序（ O(n<sup>2</sup>) ）——流行的排序算法

~~~
BUBBLE-SORT(A)
	for i ← 1 to length[A]
		for j ← length[A] downto i+1
			if A[j] < A[j-1]
				then exchange A[j] ↔ A[j-1]
~~~

## 第3章 函数的增长
详情请看书

## 第4章 递归式
详情请看书

## 第5章 概率分析和随机算法

### 雇用问题
问题假设应聘助理工作的人编号为1到n，每天一次面试，每面试完一人，如果他比目前助理更有资格担任这个职位（假设雇主能够判断他是不是更有资格），就聘请他并解雇目前助理。假设雇用的成本要比不雇用的成本高很多，请预测这种费用将会是多少。

~~~
RANDOMIZZED-HIRE-ASSISTANT(n)
	randomly permute the list of condidate
	best ← 0  ⊳cndidate 0 is a least-qualified dummy candidate
	for i ← 1 to n
		interview condidate i
		if condidate i is better than candidate best
			then best ← i
			     hire candidate i
~~~

### 随机排列算法（RANDOM()为选取随机数的函数）

#### 排序随机排列（Θ(nlgn)）

~~~
PERMUTE-BY-SORTING(A)
	n ← length[A]
	for i ← 1 to n
		P[i] = RANDOM(1, n^3)
	sort A, using P as sort keys
	return A
~~~

为数组的每一个元素A[i]赋一个随机的优先级P[i]，然后根据优先级对数组A中的元素进行排序

#### 原地随机排列（Θ(n)）

~~~
RANDOMIZE-IN-PLACE(A)
	n ← length[A]
	for i ← 1 to n
		swap A[i] ↔ A[RANDOM(i,n)]
~~~

在第i次迭代时，从元素A[i]到A[n]中随机选取一个替换元素A[i]。第i次迭代后，A[i]保持不变

# 第二部分 排序和顺序统计学

## 第6章 堆排序

### 完全二叉树各子树下标的计算方法（Θ(1)）

~~~
PARENT(i)
	return ⌊i/2⌋
LEFT(i)
	return 2i
RIGHT(i)
	return 2i+1
~~~

在大多数计算机上，上面过程可以在一条指令内计算出来，将i的二进制表示右移和左移一位能分别实现PARENT()和LEFT()

### 保持堆的性质（O(lgn)）

~~~
MAX-HEAPIFY(A, i)
	l ← LEFT(i)
	r ← RIGHT(i)
	if l≤heap-size[A] and A[l]>A[i]
		then largest ← l
		else largest ← i
	if r≤heap-size[A] and A[l]>A[i]
		then largest ← r
	if largest≠i
		then exchange A[i]↔A[largest]
		     MAX-HEAPIFY(A, largest)
~~~

MAX-HEAPIFY让A[i]在最大堆中“下降”，使以i为根的子树成为最大堆（假设以LEFT(i)和RIGHT(i)为根的两棵二叉树都是最大堆）。heap-size返回二叉树A的大小。

### 建堆（O(n)）

~~~
BUILD-MAX-HEAP(A)
	heap-size[A] ← length[A]
	for i ← ⌊length[A]/2⌋ downto 1
		MAX-HEAPIFY(A, i)
~~~

BUILD-MAX-HEAP通过自底向上地用MAX-HEAPIFY，将数组A[1..n]（此处n=length[A]）变成最大堆

### 堆排序算法（O(nlgn)）

~~~
HEAPSORT(A)
	BUILD-MAX-HEAP(A)
	for i ← length[A] downto 2
		exchange A[1]↔A[i]
		heap-size[A] ← heap-size[A]-1
		MAX-HEAPIFY(A, 1)
~~~

### 优先级队列
暂略

## 第7章 快速排序

### 快速排序的描述
快速排序也是基于分治模式的。下面是对一个典型子数组A[p..r]排序的分治过程的三个步骤：

~~~
分解：数组A[p..r]被划分成两个子数组（可能为空）A[p..q-1]和A[q+1..r]，使得A[p..q-1]中的每个元素都小于A(q)，而且，小于等于A[q+1..r]中的元素。下标q也在这个划分过程中进行计算。
解决：通过递归调用快速排序，对子数组A[p..q-1]和A[q+1..r]排序
合并：因为两个子数组是就地排序的，将它们合并不需要操作：整个数组A[p..r]已排序
~~~

### 快速排序的算法（最坏：Θ(n<sup>2</sup>)，最佳：O(nlgn)，平均：O(nlgn)）

~~~
QUICKSORT(A, p, r)
	if p<r
		then q ← PARTITION(A, p, r)
		     QUICKSORT(A, p, q-1)
		     QUICKSORT(A, q+1, r)
~~~

调用QUICKSORT(A, 1, length[A])即可对数组A完成排序

### 数组划分（Θ(n)）

~~~
PARTITION(A, p, r)
	x ← A[r]
	i ← p-1
	for j ← p to r-1
		if A[j]≤x
			then i ← i+1
			     exchange A[i]↔A[j]
	exchange A[i+1]↔A[r]
	return i+1
~~~

PARTITION以x(=A[r])作为主元(pivot element)，对子数组A[p..r]进行就地重排。在此过程中A[p..i]中的各个值都小于或等于x，A[i+1..j-1]中的值都大于x，A[r]=x。A[j..r-1]中的值可以取任何值。

### 快速排序的随机化版本
对于有的算法，我们可以向其加入随机化的成分，以便对于所有输入，它均能获得较好的平均情况下的性能

#### 划分的随机化算法（Θ(n)）

~~~
RANDOMIZED-PARTITION(A, p, r)
	i ← RANDOM(p, r)
	exchange A[r]↔A[i]
	return PARTIONTION(A, p, r)
~~~

随机取样(random sampling)是一种随机化技术。在这种方法中，不是始终采用A[r]作为主元，而是从子数组A[p..r]中随机选择一个元素，即将A[r]与从A[p..r]中随机选出的一个元素交换（因为主元元素是随机选择的，我们期望在平均情况下，对输入数组的划分能够比较对称）。

新的快速排序过程中不再调用PARTITIOIN，而是调用RANDOMIZED-PARTITION。

### 快速排序的运行时间分析
详情请看书

## 第8章 线性时间排序

### 计数排序
暂略

### 基数排序
暂略

### 比较排序算法运行时间的下界为什么是Ω(nlgn)
暂略

## 第9章 中位数和顺序统计学
再略



# 书上用过的符号
∞ Ω ω ∈ π φ Φ Ø ⊳ ⊲ ↕ Θ ⌊⌋ ⌈⌉ ≈ ≠ ≥ ≤ ↔ ← ×
