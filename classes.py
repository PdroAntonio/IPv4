import re


class CalcIPv4:
    def __init__(self, ip, masc=None, prefixo=None):
        self.ip = ip
        self.masc = masc
        self.prefixo = prefixo

        self._set_broadcast()
        self._set_rede()

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def n_ips(self):
        return self._get_n_ips()

    @property
    def ip(self):
        return self._ip

    @property
    def masc(self):
        return self._masc

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, v):
        if not self._valida_ip(v):
            raise ValueError('IP inválido.')

        self._ip = v
        self._ip_bin = self._ip_to_bin(v)

    @masc.setter
    def masc(self, v):
        if not v:
            return

        if not self._valida_ip(v):
            raise ValueError('Máscara inválida.')

        self._masc = v
        self._masc_bin = self._ip_to_bin(v)

        if not hasattr(self, 'prefixo'):
            self.prefixo = self._masc_bin.count('1')

    @prefixo.setter
    def prefixo(self, v):
        if not v:
            return

        if not isinstance(v, int):
            raise TypeError('Prefixo precisa ser inteiro.')

        if v > 32:
            raise TypeError('Prefixo precisa ter 32 bits.')

        self._prefixo = v
        self._masc_bin = (v * '1').ljust(32, '0')
        if not hasattr(self, 'masc'):
            self.masc = self._bin_to_ip(self._masc_bin)

    @staticmethod
    def _valida_ip(_ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )
        if regexp.search(_ip):
            return True

    @staticmethod
    def _ip_to_bin(_ip):
        blocos = _ip.split('.')
        blocos_bin = [bin(int(x))[2:].zfill(8) for x in blocos]
        return ''.join(blocos_bin)

    @staticmethod
    def _bin_to_ip(_ip):
        n = 8
        blocos = [str(int(_ip[i:n+i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._rede

    def _get_n_ips(self):
        return 2 ** (32 - self.prefixo)