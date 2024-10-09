#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

d1 = datetime.now()
print(d1)
print(d1.year, d1.month, d1.day, d1.hour, d1.minute, d1.second)

d2 = datetime(2000, 1, 1, 0, 0, 0)
print(d2)

diff = d1 - d2
print(diff)

print(diff.days, diff.seconds)

print(datetime(2000, 1, 1) < timedelta(2000, 1, 2))

print(timedelta(1) < timedelta(2))
print(datetime(2000, 1, 1) + timedelta(10))
