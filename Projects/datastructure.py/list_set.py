def set_value(self, inde, value):
    temp = self.get(index)
    if temp is not None:
        temp.value = value
        return True
    return False
    
    # for _ in range(index):
        # 