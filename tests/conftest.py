import pytest


@pytest.fixture
def result_data():
    """Return a list of result tuples, (id, down, timestamp)."""
    return [
        (4, False, 1499333281),
        (4, True, 1499336881),
        (2, False, 1499340481),
        (1, False, 1499344081),
        (0, True, 1499347681),
        (4, True, 1499351281),
        (1, False, 1499354881),
        (4, True, 1499358481),
        (4, True, 1499362081),
        (1, False, 1499365681),
        (0, True, 1499369281),
        (2, True, 1499372881),
        (1, False, 1499376481),
        (0, False, 1499380081),
        (1, False, 1499383681),
        (3, True, 1499387281),
        (3, False, 1499390881),
        (2, False, 1499394481),
        (4, False, 1499398081),
        (3, False, 1499401681),
        (1, False, 1499405281),
        (4, False, 1499408881),
        (1, False, 1499412481),
        (2, True, 1499416081),
        (1, False, 1499419681),
        (2, False, 1499423281),
        (3, False, 1499426881),
        (3, False, 1499430481),
        (0, True, 1499434081),
        (3, False, 1499437681),
        (2, False, 1499441281),
        (4, True, 1499444881),
        (2, False, 1499448481),
        (0, True, 1499452081),
        (3, False, 1499455681),
        (2, False, 1499459281),
        (3, True, 1499462881),
        (0, True, 1499466481),
        (1, True, 1499470081),
        (0, False, 1499473681),
        (3, True, 1499477281),
        (1, True, 1499480881),
        (0, True, 1499484481),
        (0, False, 1499488081),
        (4, True, 1499491681),
        (2, False, 1499495281),
        (0, True, 1499498881),
        (3, False, 1499502481),
        (0, True, 1499506081),
        (0, True, 1499509681),
        (2, True, 1499513281),
        (4, False, 1499516881),
        (3, False, 1499520481),
        (3, False, 1499524081),
        (2, False, 1499527681),
        (3, True, 1499531281),
        (4, True, 1499534881),
        (4, False, 1499538481),
        (0, False, 1499542081),
        (0, False, 1499545681),
        (3, False, 1499549281),
        (2, True, 1499552881),
        (0, True, 1499556481),
        (1, True, 1499560081),
        (1, True, 1499563681),
        (3, True, 1499567281),
        (3, True, 1499570881),
        (0, False, 1499574481),
        (1, False, 1499578081),
        (1, False, 1499581681),
        (2, False, 1499585281),
        (0, False, 1499588881),
        (2, True, 1499592481),
        (4, True, 1499596081),
        (4, True, 1499599681),
        (2, True, 1499603281),
        (2, True, 1499606881),
        (0, False, 1499610481),
        (0, False, 1499614081),
        (1, False, 1499617681),
        (1, False, 1499621281),
        (1, False, 1499624881),
        (0, True, 1499628481),
        (4, False, 1499632081),
        (3, False, 1499635681),
        (4, False, 1499639281),
        (0, True, 1499642881),
        (4, True, 1499646481),
        (3, True, 1499650081),
        (0, True, 1499653681),
        (1, True, 1499657281),
        (4, True, 1499660881),
        (4, True, 1499664481),
        (1, True, 1499668081),
        (3, False, 1499671681),
        (2, False, 1499675281),
        (1, True, 1499678881),
        (3, False, 1499682481),
        (2, False, 1499686081),
        (0, True, 1499689681)
    ]


@pytest.fixture
def range_data():
    """Return tuples like (id, previous, results, next)."""
    return [
        (0,
         None,
         [1499347681, 1499369281],
         1499380081),
        (3,
            None,
            [1499387281],
            1499390881),
        (2,
            1499340481,
            [1499372881],
            1499394481),
        (4,
            1499333281,
            [1499336881, 1499351281, 1499358481, 1499362081],
            1499398081),
        (2,
            1499394481,
            [1499416081],
            1499423281),
        (0,
            1499380081,
            [1499434081, 1499452081, 1499466481],
            1499473681),
        (0,
            1499473681,
            [1499484481],
            1499488081),
        (3,
            1499455681,
            [1499462881, 1499477281],
            1499502481),
        (4,
            1499408881,
            [1499444881, 1499491681],
            1499516881),
        (2,
            1499495281,
            [1499513281],
            1499527681),
        (4,
            1499516881,
            [1499534881],
            1499538481),
        (0,
            1499488081,
            [1499498881, 1499506081, 1499509681],
            1499542081),
        (3,
            1499524081,
            [1499531281],
            1499549281),
        (0,
            1499545681,
            [1499556481],
            1499574481),
        (1,
            1499419681,
            [1499470081, 1499480881, 1499560081, 1499563681],
            1499578081),
        (2,
            1499527681,
            [1499552881],
            1499585281),
        (4,
            1499538481,
            [1499596081, 1499599681],
            1499632081),
        (3,
            1499549281,
            [1499567281, 1499570881],
            1499635681),
        (3,
            1499635681,
            [1499650081],
            1499671681),
        (2,
            1499585281,
            [1499592481, 1499603281, 1499606881],
            1499675281),
        (0,
            1499614081,
            [1499628481, 1499642881, 1499653681, 1499689681],
            None),
        (1,
            1499624881,
            [1499657281, 1499668081, 1499678881],
            None),
        (4,
            1499639281,
            [1499646481, 1499660881, 1499664481],
            None)
    ]


@pytest.fixture
def outage_data():
    return [
        (None, 1499369281),
        (None, 1499387281),
        (1499372881, 1499372881),
        (1499336881, 1499362081),
        (1499416081, 1499416081),
        (1499434081, 1499466481),
        (1499484481, 1499484481),
        (1499462881, 1499477281),
        (1499444881, 1499491681),
        (1499513281, 1499513281),
        (1499534881, 1499534881),
        (1499498881, 1499509681),
        (1499531281, 1499531281),
        (1499556481, 1499556481),
        (1499470081, 1499563681),
        (1499552881, 1499552881),
        (1499596081, 1499599681),
        (1499567281, 1499570881),
        (1499650081, 1499650081),
        (1499592481, 1499606881),
        (1499628481, None),
        (1499657281, None),
        (1499646481, None),
    ]
