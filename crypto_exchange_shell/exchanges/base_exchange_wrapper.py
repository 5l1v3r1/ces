# Copyright (c) 2018, Matias Fontanini
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of the FreeBSD Project.

from crypto_exchange_shell.exceptions import *

class BaseExchangeWrapper:
    def __init__(self):
        self._currencies = {}
        self._markets = {}

    def add_currency(self, currency):
        self._currencies[currency.code] = currency

    def add_market(self, base_currency_code, market_currency_code):
        if base_currency_code not in self._markets:
            self._markets[base_currency_code] = set()
        self._markets[base_currency_code].add(market_currency_code)

    def get_base_currencies(self):
        return [self._currencies[x] for x in self._markets.keys()]

    def get_currencies(self):
        return self._currencies.values()

    def get_markets(self, base_currency_code):
        if base_currency_code not in self._markets:
            raise InvalidArgumentException('Invalid base currency {0}'.format(base_currency_code))
        return [self._currencies[x] for x in self._markets[base_currency_code]]