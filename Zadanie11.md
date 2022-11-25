Osoba.objects.all()
    returns <QuerySet [<Osoba: Osoba1>, <Osoba: Osoba2>, <Osoba: Osoba3>]>

    Osoba.objects.filter(id=3)
    <QuerySet [<Osoba: Karol Wodzirej>]>

    Osoba.objects.filter(id=1)
    <QuerySet [<Osoba: Mariusz Krawczyk>]>

    Osoba.objects.order_by().values('druzyna').distinct()
    <QuerySet [{'druzyna': Lech Poznan (PL)}, {'druzyna': Legia Warszawa (PL)}]>

    Druzyna.objects.order_by('-nazwa')
    <QuerySet [<Druzyna: Lech Poznan (PL)>, <Druzyna: Legia Warszawa (PL)>]>