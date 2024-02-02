from example_module import foo
from example_packet import example_packet_module1
from example_packet import example_packet_module2


def super_foo():
    foo()
    example_packet_module1.packet_foo1()
    example_packet_module2.packet_foo2()


if __name__ == "__main__":
    super_foo()
