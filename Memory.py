class MemoryStack:

    def __init__(self, memory=None):    # initialize memory stack with memory <memory>
        self.mem_dict = {}
        self.stacks = []
        self.stacks.append(self.mem_dict)
        self.stack_counter = 0

    def get(self, name):                # gets from memory stack current value of variable <name>
        value = None
        for stack in self.stacks:
            value = stack.get(name)
            if value is not None:
                return value

    def insert(self, name, value):      # inserts into memory stack variable <name> with value <value>
        for stack in self.stacks:
            if name in stack.keys():
                stack[name] = value

        self.stacks[self.stack_counter][name] = value

    def set(self, name, value):         # sets variable <name> to value <value>
        for stack in self.stacks:
            if name in stack.keys():
                stack[name] = value

        self.stacks[self.stack_counter][name] = value

    def push(self):             # pushes memory <memory> onto the stack
        mem_stack = {}
        self.stack_counter += 1
        self.stacks.append(mem_stack)

    def pop(self):
        self.stacks.pop(self.stack_counter)
        self.stack_counter -= 1

