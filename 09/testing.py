import weakref
import cProfile
import pstats
import io
from memory_profiler import profile


def profile_deco(function):
    class wrap_test():

        def __init__(self, function) -> None:
            self.function = function
            self.profile_results = ''

        def __call__(self, *args, **kwds):
            pr_ = cProfile.Profile()
            pr_.enable()
            self.function(*args, **kwds)
            pr_.disable()
            s_ = io.StringIO()
            sortby = "cumulative"
            ps_ = pstats.Stats(pr_, stream=s_).sort_stats(sortby)
            ps_.print_stats()
            self.profile_results += s_.getvalue()
            return self

        def print_stat(self):
            print(self.profile_results)
    return wrap_test(function)


class EngineWeak():
    def __init__(self, car):
        self.car = weakref.ref(car)
        self.data_obj = ['K']*750


class CarWeak():

    def __init__(self):
        self.engine1 = EngineWeak(self)
        self.engine2 = EngineWeak(self)
        self.engine3 = EngineWeak(self)
        self.engine4 = EngineWeak(self)
        self.engine5 = EngineWeak(self)

    def car_testing(self):
        for i in [1, 2, 3, 4, 5]:
            for _ in getattr(self, f'engine{i}').data_obj:
                pass


class Engine():
    def __init__(self, car):
        self.car = car
        self.data_obj = ['K']*750


class Car():

    def __init__(self):
        self.engine1 = Engine(self)
        self.engine2 = Engine(self)
        self.engine3 = Engine(self)
        self.engine4 = Engine(self)
        self.engine5 = Engine(self)

    def car_testing(self):
        for i in [1, 2, 3, 4, 5]:
            for _ in getattr(self, f'engine{i}').data_obj:
                pass


class EngineSlots():

    def __init__(self, car):
        self.car = car
        self.data_obj = ['K']*750


class CarSlots():
    __slots__ = ("engine1", "engine2", "engine3", "engine4", "engine5")

    def __init__(self):
        self.engine1 = EngineSlots(self)
        self.engine2 = EngineSlots(self)
        self.engine3 = EngineSlots(self)
        self.engine4 = EngineSlots(self)
        self.engine5 = EngineSlots(self)

    def car_testing(self):
        for i in [1, 2, 3, 4, 5]:
            for _ in getattr(self, f'engine{i}').data_obj:
                pass


obj_common = [Car() for _ in range(750)]
obj_weak = [CarWeak() for _ in range(750)]
obj_slots = [CarSlots() for _ in range(750)]


@profile_deco
def test_create_common():
    obj_s = [Car() for _ in range(750)]
    for obj in obj_s:
        obj.car_testing()
    del obj_s


@profile_deco
def test_create_weak():
    obj_s = [CarWeak() for _ in range(750)]
    for obj in obj_s:
        obj.car_testing()
    del obj_s


@profile_deco
def test_create_slots():
    obj_s = [CarSlots() for _ in range(750)]
    for obj in obj_s:
        obj.car_testing()
    del obj_s


def test_edit_common():
    for obj in obj_common:
        obj.engine2 = '3'


def test_edit_weak():
    for obj in obj_weak:
        obj.engine2 = '3'


@profile
def all_test_memory_profile():
    test_create_common()
    test_create_weak()
    test_create_slots()
    test_edit_common()
    test_edit_weak()


if __name__ == "__main__":
    all_test_memory_profile()
    COMMON_ = test_create_common()
    SLOTS_ = test_create_weak()
    WEAK_ = test_create_slots()
    COMMON_.print_stat()
    SLOTS_.print_stat()
    WEAK_.print_stat()
