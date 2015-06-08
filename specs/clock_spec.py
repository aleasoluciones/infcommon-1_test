# -*- coding: utf-8 -*-

from doublex import *
from expects import *
from doublex_expects import *

import datetime

from infcommon import clock as clock_module

with description('Clock specs'):
    with it('calls collaborator for today'):
        date_obj = Spy()
        clock = clock_module.Clock(date_obj=date_obj)
        clock.today()
        expect(date_obj.today).to(have_been_called)

    with it('calls collaborator for now'):
        datetime_obj = Spy()
        clock = clock_module.Clock(datetime_obj=datetime_obj)
        clock.now()
        expect(datetime_obj.now).to(have_been_called)

    with it('calls collaborator for utcnow'):
        datetime_obj = Spy()
        clock = clock_module.Clock(datetime_obj=datetime_obj)
        clock.utcnow()
        expect(datetime_obj.utcnow).to(have_been_called)

    with context('working with timestamps'):
        with it('checks aproximated time stamps'):
            now = clock_module.Clock().now()
            utc_timestamp = clock_module.Clock().utctimestampnow()
            local_from_timestamp = clock_module.Clock.fromtimestamp(utc_timestamp)
            expect(clock_module.Clock.aprox(now, local_from_timestamp)).to(be_true)

        with context('using conversion'):
            with it('checks aproximated timestamps '):
                # This conversion loose some microseconds so we only check if the
                # conversion is approximately correct
                now = datetime.datetime.now()
                ts = clock_module.Clock.timestamp(now)
                now_from_ts = clock_module.Clock.fromtimestamp(ts)
                expect(clock_module.Clock.aprox(now, now_from_ts)).to(be_true)

