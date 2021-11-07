class Stack1:
    def __init__(self, size=10000):
        self.arr = [None] * size #array 늘리고 줄이는 연산보다 미리 메모리 할당시켜놓아서 효율적임
        self.last_index = 0 #현재 사용할 수 있는 인덱스

    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index +=1

    def pop(self):
        # 뒤(위)에서 뽑기

        if self.empty():
            raise Exception('Stack is empty')
        self.last_index = self.last_index-1
        return self.arr[self.last_index]

    def empty(self):
        if self.last_index ==0:
            return True
        else:
            return False

    def peek(self):
        #가장 마지막번째 값을 index 값 안 바꾸고 출력
        if self.empty():
            raise Exception("Stack is empty")
        return self.arr[self.last_index-1]

st = Stack1(100)
st.push(20)
print(st.peek())