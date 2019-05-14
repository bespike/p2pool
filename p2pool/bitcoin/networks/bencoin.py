import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 6333
ADDRESS_VERSION = 27
RPC_PORT = 6332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, 'dc4ac386ea807072aa940a6bf1f89d7d5e18ab71c646c85377984ef762e5c639')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'BEC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'bencoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/bencoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bencoin'), 'bencoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://benjamin-wilson.co.uk/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://benjamin-wilson.co.uk/address/'
TX_EXPLORER_URL_PREFIX = 'http://benjamin-wilson.co.uk/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
