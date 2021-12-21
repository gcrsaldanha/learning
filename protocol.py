from typing import Iterable, Protocol, runtime_checkable


@runtime_checkable
class Payable(Protocol):
    def pay(self) -> None:
        ...


class CreditCard:
    def pay(self) -> None:
        print("Paying with credit card...")


class Wire:
    def pay(self) -> None:
        print("Paying with wire transfer...")


def pay_with_fallback(payables: Iterable[Payable]) -> None:
    for payable in payables:
        payable.pay()

card = CreditCard()
wire = Wire()

assert issubclass(CreditCard, Payable)
assert issubclass(Wire, Payable)
assert isinstance(card, Payable)
assert isinstance(wire, Payable)

pay_with_fallback([card, wire])
pay_with_fallback([1])
