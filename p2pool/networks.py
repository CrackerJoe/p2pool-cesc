from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
   	cryptoescudo=math.Object(
        PARENT=networks.nets['cryptoescudo'],
        SHARE_PERIOD=14, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=15, # blocks
        IDENTIFIER='12AAB76FF9773259'.decode('hex'),
        PREFIX='12AAB76FF9773257'.decode('hex'),
        P2P_PORT=7576,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=7575,
        BOOTSTRAP_ADDRS='176.111.108.151'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool.pt',
        VERSION_CHECK=lambda v: True,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
