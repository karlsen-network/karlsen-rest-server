# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: p2p.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tp2p.proto\x12\tprotowire\"g\n\x17RequestAddressesMessage\x12\x1d\n\x15includeAllSubnetworks\x18\x01 \x01(\x08\x12-\n\x0csubnetworkId\x18\x02 \x01(\x0b\x32\x17.protowire.SubnetworkId\">\n\x10\x41\x64\x64ressesMessage\x12*\n\x0b\x61\x64\x64ressList\x18\x01 \x03(\x0b\x32\x15.protowire.NetAddress\"9\n\nNetAddress\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\n\n\x02ip\x18\x03 \x01(\x0c\x12\x0c\n\x04port\x18\x04 \x01(\r\"\x1d\n\x0cSubnetworkId\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\"\xe0\x01\n\x12TransactionMessage\x12\x0f\n\x07version\x18\x01 \x01(\r\x12+\n\x06inputs\x18\x02 \x03(\x0b\x32\x1b.protowire.TransactionInput\x12-\n\x07outputs\x18\x03 \x03(\x0b\x32\x1c.protowire.TransactionOutput\x12\x10\n\x08lockTime\x18\x04 \x01(\x04\x12-\n\x0csubnetworkId\x18\x05 \x01(\x0b\x32\x17.protowire.SubnetworkId\x12\x0b\n\x03gas\x18\x06 \x01(\x04\x12\x0f\n\x07payload\x18\x08 \x01(\x0c\"\x80\x01\n\x10TransactionInput\x12-\n\x10previousOutpoint\x18\x01 \x01(\x0b\x32\x13.protowire.Outpoint\x12\x17\n\x0fsignatureScript\x18\x02 \x01(\x0c\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x12\n\nsigOpCount\x18\x04 \x01(\r\"J\n\x08Outpoint\x12/\n\rtransactionId\x18\x01 \x01(\x0b\x32\x18.protowire.TransactionId\x12\r\n\x05index\x18\x02 \x01(\r\"\x1e\n\rTransactionId\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\"2\n\x0fScriptPublicKey\x12\x0e\n\x06script\x18\x01 \x01(\x0c\x12\x0f\n\x07version\x18\x02 \x01(\r\"W\n\x11TransactionOutput\x12\r\n\x05value\x18\x01 \x01(\x04\x12\x33\n\x0fscriptPublicKey\x18\x02 \x01(\x0b\x32\x1a.protowire.ScriptPublicKey\"k\n\x0c\x42lockMessage\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.protowire.BlockHeader\x12\x33\n\x0ctransactions\x18\x02 \x03(\x0b\x32\x1d.protowire.TransactionMessage\"\xdc\x02\n\x0b\x42lockHeader\x12\x0f\n\x07version\x18\x01 \x01(\r\x12-\n\x07parents\x18\x0c \x03(\x0b\x32\x1c.protowire.BlockLevelParents\x12\'\n\x0ehashMerkleRoot\x18\x03 \x01(\x0b\x32\x0f.protowire.Hash\x12-\n\x14\x61\x63\x63\x65ptedIdMerkleRoot\x18\x04 \x01(\x0b\x32\x0f.protowire.Hash\x12\'\n\x0eutxoCommitment\x18\x05 \x01(\x0b\x32\x0f.protowire.Hash\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\x12\x0c\n\x04\x62its\x18\x07 \x01(\r\x12\r\n\x05nonce\x18\x08 \x01(\x04\x12\x10\n\x08\x64\x61\x61Score\x18\t \x01(\x04\x12\x10\n\x08\x62lueWork\x18\n \x01(\x0c\x12%\n\x0cpruningPoint\x18\x0e \x01(\x0b\x32\x0f.protowire.Hash\x12\x11\n\tblueScore\x18\r \x01(\x04\":\n\x11\x42lockLevelParents\x12%\n\x0cparentHashes\x18\x01 \x03(\x0b\x32\x0f.protowire.Hash\"\x15\n\x04Hash\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\"N\n\x1aRequestBlockLocatorMessage\x12!\n\x08highHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12\r\n\x05limit\x18\x02 \x01(\r\"6\n\x13\x42lockLocatorMessage\x12\x1f\n\x06hashes\x18\x01 \x03(\x0b\x32\x0f.protowire.Hash\"\\\n\x15RequestHeadersMessage\x12 \n\x07lowHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12!\n\x08highHash\x18\x02 \x01(\x0b\x32\x0f.protowire.Hash\"\x1b\n\x19RequestNextHeadersMessage\"\x14\n\x12\x44oneHeadersMessage\"<\n\x19RequestRelayBlocksMessage\x12\x1f\n\x06hashes\x18\x01 \x03(\x0b\x32\x0f.protowire.Hash\"C\n\x1aRequestTransactionsMessage\x12%\n\x03ids\x18\x01 \x03(\x0b\x32\x18.protowire.TransactionId\"B\n\x1aTransactionNotFoundMessage\x12$\n\x02id\x18\x01 \x01(\x0b\x32\x18.protowire.TransactionId\"5\n\x14InvRelayBlockMessage\x12\x1d\n\x04hash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\"?\n\x16InvTransactionsMessage\x12%\n\x03ids\x18\x01 \x03(\x0b\x32\x18.protowire.TransactionId\"\x1c\n\x0bPingMessage\x12\r\n\x05nonce\x18\x01 \x01(\x04\"\x1c\n\x0bPongMessage\x12\r\n\x05nonce\x18\x01 \x01(\x04\"\x0f\n\rVerackMessage\"\xed\x01\n\x0eVersionMessage\x12\x17\n\x0fprotocolVersion\x18\x01 \x01(\r\x12\x10\n\x08services\x18\x02 \x01(\x04\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.protowire.NetAddress\x12\n\n\x02id\x18\x05 \x01(\x0c\x12\x11\n\tuserAgent\x18\x06 \x01(\t\x12\x16\n\x0e\x64isableRelayTx\x18\x08 \x01(\x08\x12-\n\x0csubnetworkId\x18\t \x01(\x0b\x32\x17.protowire.SubnetworkId\x12\x0f\n\x07network\x18\n \x01(\t\"\x1f\n\rRejectMessage\x12\x0e\n\x06reason\x18\x01 \x01(\t\"N\n!RequestPruningPointUTXOSetMessage\x12)\n\x10pruningPointHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\"i\n\x1fPruningPointUtxoSetChunkMessage\x12\x46\n\x19outpointAndUtxoEntryPairs\x18\x01 \x03(\x0b\x32#.protowire.OutpointAndUtxoEntryPair\"j\n\x18OutpointAndUtxoEntryPair\x12%\n\x08outpoint\x18\x01 \x01(\x0b\x32\x13.protowire.Outpoint\x12\'\n\tutxoEntry\x18\x02 \x01(\x0b\x32\x14.protowire.UtxoEntry\"{\n\tUtxoEntry\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x04\x12\x33\n\x0fscriptPublicKey\x18\x02 \x01(\x0b\x32\x1a.protowire.ScriptPublicKey\x12\x15\n\rblockDaaScore\x18\x03 \x01(\x04\x12\x12\n\nisCoinbase\x18\x04 \x01(\x08\",\n*RequestNextPruningPointUtxoSetChunkMessage\"&\n$DonePruningPointUtxoSetChunksMessage\":\n\x17RequestIBDBlocksMessage\x12\x1f\n\x06hashes\x18\x01 \x03(\x0b\x32\x0f.protowire.Hash\"\x1f\n\x1dUnexpectedPruningPointMessage\"j\n\x16IbdBlockLocatorMessage\x12#\n\ntargetHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12+\n\x12\x62lockLocatorHashes\x18\x02 \x03(\x0b\x32\x0f.protowire.Hash\"i\n\"RequestIBDChainBlockLocatorMessage\x12 \n\x07lowHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12!\n\x08highHash\x18\x02 \x01(\x0b\x32\x0f.protowire.Hash\"J\n\x1bIbdChainBlockLocatorMessage\x12+\n\x12\x62lockLocatorHashes\x18\x01 \x03(\x0b\x32\x0f.protowire.Hash\"b\n\x16RequestAnticoneMessage\x12\"\n\tblockHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12$\n\x0b\x63ontextHash\x18\x02 \x01(\x0b\x32\x0f.protowire.Hash\"I\n!IbdBlockLocatorHighestHashMessage\x12$\n\x0bhighestHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\"+\n)IbdBlockLocatorHighestHashNotFoundMessage\"C\n\x13\x42lockHeadersMessage\x12,\n\x0c\x62lockHeaders\x18\x01 \x03(\x0b\x32\x16.protowire.BlockHeader\"*\n(RequestPruningPointAndItsAnticoneMessage\"4\n2RequestNextPruningPointAndItsAnticoneBlocksMessage\"\xbb\x01\n\x1b\x42lockWithTrustedDataMessage\x12&\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x17.protowire.BlockMessage\x12\x10\n\x08\x64\x61\x61Score\x18\x02 \x01(\x04\x12&\n\tdaaWindow\x18\x03 \x03(\x0b\x32\x13.protowire.DaaBlock\x12:\n\x0cghostdagData\x18\x04 \x03(\x0b\x32$.protowire.BlockGhostdagDataHashPair\"a\n\x08\x44\x61\x61\x42lock\x12&\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x17.protowire.BlockMessage\x12-\n\x0cghostdagData\x18\x02 \x01(\x0b\x32\x17.protowire.GhostdagData\"c\n\nDaaBlockV4\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.protowire.BlockHeader\x12-\n\x0cghostdagData\x18\x02 \x01(\x0b\x32\x17.protowire.GhostdagData\"i\n\x19\x42lockGhostdagDataHashPair\x12\x1d\n\x04hash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12-\n\x0cghostdagData\x18\x02 \x01(\x0b\x32\x17.protowire.GhostdagData\"\xe6\x01\n\x0cGhostdagData\x12\x11\n\tblueScore\x18\x01 \x01(\x04\x12\x10\n\x08\x62lueWork\x18\x02 \x01(\x0c\x12\'\n\x0eselectedParent\x18\x03 \x01(\x0b\x32\x0f.protowire.Hash\x12&\n\rmergeSetBlues\x18\x04 \x03(\x0b\x32\x0f.protowire.Hash\x12%\n\x0cmergeSetReds\x18\x05 \x03(\x0b\x32\x0f.protowire.Hash\x12\x39\n\x12\x62luesAnticoneSizes\x18\x06 \x03(\x0b\x32\x1d.protowire.BluesAnticoneSizes\"M\n\x12\x42luesAnticoneSizes\x12!\n\x08\x62lueHash\x18\x01 \x01(\x0b\x32\x0f.protowire.Hash\x12\x14\n\x0c\x61nticoneSize\x18\x02 \x01(\r\"\"\n DoneBlocksWithTrustedDataMessage\"?\n\x14PruningPointsMessage\x12\'\n\x07headers\x18\x01 \x03(\x0b\x32\x16.protowire.BlockHeader\"!\n\x1fRequestPruningPointProofMessage\"T\n\x18PruningPointProofMessage\x12\x38\n\x07headers\x18\x01 \x03(\x0b\x32\'.protowire.PruningPointProofHeaderArray\"G\n\x1cPruningPointProofHeaderArray\x12\'\n\x07headers\x18\x01 \x03(\x0b\x32\x16.protowire.BlockHeader\"\x0e\n\x0cReadyMessage\"~\n\x1d\x42lockWithTrustedDataV4Message\x12&\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x17.protowire.BlockMessage\x12\x18\n\x10\x64\x61\x61WindowIndices\x18\x02 \x03(\x04\x12\x1b\n\x13ghostdagDataIndices\x18\x03 \x03(\x04\"z\n\x12TrustedDataMessage\x12(\n\tdaaWindow\x18\x01 \x03(\x0b\x32\x15.protowire.DaaBlockV4\x12:\n\x0cghostdagData\x18\x02 \x03(\x0b\x32$.protowire.BlockGhostdagDataHashPairB/Z-github.com/karlsen-network/karlsend/protowireb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'p2p_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/karlsen-network/karlsend/protowire'
  _globals['_REQUESTADDRESSESMESSAGE']._serialized_start=24
  _globals['_REQUESTADDRESSESMESSAGE']._serialized_end=127
  _globals['_ADDRESSESMESSAGE']._serialized_start=129
  _globals['_ADDRESSESMESSAGE']._serialized_end=191
  _globals['_NETADDRESS']._serialized_start=193
  _globals['_NETADDRESS']._serialized_end=250
  _globals['_SUBNETWORKID']._serialized_start=252
  _globals['_SUBNETWORKID']._serialized_end=281
  _globals['_TRANSACTIONMESSAGE']._serialized_start=284
  _globals['_TRANSACTIONMESSAGE']._serialized_end=508
  _globals['_TRANSACTIONINPUT']._serialized_start=511
  _globals['_TRANSACTIONINPUT']._serialized_end=639
  _globals['_OUTPOINT']._serialized_start=641
  _globals['_OUTPOINT']._serialized_end=715
  _globals['_TRANSACTIONID']._serialized_start=717
  _globals['_TRANSACTIONID']._serialized_end=747
  _globals['_SCRIPTPUBLICKEY']._serialized_start=749
  _globals['_SCRIPTPUBLICKEY']._serialized_end=799
  _globals['_TRANSACTIONOUTPUT']._serialized_start=801
  _globals['_TRANSACTIONOUTPUT']._serialized_end=888
  _globals['_BLOCKMESSAGE']._serialized_start=890
  _globals['_BLOCKMESSAGE']._serialized_end=997
  _globals['_BLOCKHEADER']._serialized_start=1000
  _globals['_BLOCKHEADER']._serialized_end=1348
  _globals['_BLOCKLEVELPARENTS']._serialized_start=1350
  _globals['_BLOCKLEVELPARENTS']._serialized_end=1408
  _globals['_HASH']._serialized_start=1410
  _globals['_HASH']._serialized_end=1431
  _globals['_REQUESTBLOCKLOCATORMESSAGE']._serialized_start=1433
  _globals['_REQUESTBLOCKLOCATORMESSAGE']._serialized_end=1511
  _globals['_BLOCKLOCATORMESSAGE']._serialized_start=1513
  _globals['_BLOCKLOCATORMESSAGE']._serialized_end=1567
  _globals['_REQUESTHEADERSMESSAGE']._serialized_start=1569
  _globals['_REQUESTHEADERSMESSAGE']._serialized_end=1661
  _globals['_REQUESTNEXTHEADERSMESSAGE']._serialized_start=1663
  _globals['_REQUESTNEXTHEADERSMESSAGE']._serialized_end=1690
  _globals['_DONEHEADERSMESSAGE']._serialized_start=1692
  _globals['_DONEHEADERSMESSAGE']._serialized_end=1712
  _globals['_REQUESTRELAYBLOCKSMESSAGE']._serialized_start=1714
  _globals['_REQUESTRELAYBLOCKSMESSAGE']._serialized_end=1774
  _globals['_REQUESTTRANSACTIONSMESSAGE']._serialized_start=1776
  _globals['_REQUESTTRANSACTIONSMESSAGE']._serialized_end=1843
  _globals['_TRANSACTIONNOTFOUNDMESSAGE']._serialized_start=1845
  _globals['_TRANSACTIONNOTFOUNDMESSAGE']._serialized_end=1911
  _globals['_INVRELAYBLOCKMESSAGE']._serialized_start=1913
  _globals['_INVRELAYBLOCKMESSAGE']._serialized_end=1966
  _globals['_INVTRANSACTIONSMESSAGE']._serialized_start=1968
  _globals['_INVTRANSACTIONSMESSAGE']._serialized_end=2031
  _globals['_PINGMESSAGE']._serialized_start=2033
  _globals['_PINGMESSAGE']._serialized_end=2061
  _globals['_PONGMESSAGE']._serialized_start=2063
  _globals['_PONGMESSAGE']._serialized_end=2091
  _globals['_VERACKMESSAGE']._serialized_start=2093
  _globals['_VERACKMESSAGE']._serialized_end=2108
  _globals['_VERSIONMESSAGE']._serialized_start=2111
  _globals['_VERSIONMESSAGE']._serialized_end=2348
  _globals['_REJECTMESSAGE']._serialized_start=2350
  _globals['_REJECTMESSAGE']._serialized_end=2381
  _globals['_REQUESTPRUNINGPOINTUTXOSETMESSAGE']._serialized_start=2383
  _globals['_REQUESTPRUNINGPOINTUTXOSETMESSAGE']._serialized_end=2461
  _globals['_PRUNINGPOINTUTXOSETCHUNKMESSAGE']._serialized_start=2463
  _globals['_PRUNINGPOINTUTXOSETCHUNKMESSAGE']._serialized_end=2568
  _globals['_OUTPOINTANDUTXOENTRYPAIR']._serialized_start=2570
  _globals['_OUTPOINTANDUTXOENTRYPAIR']._serialized_end=2676
  _globals['_UTXOENTRY']._serialized_start=2678
  _globals['_UTXOENTRY']._serialized_end=2801
  _globals['_REQUESTNEXTPRUNINGPOINTUTXOSETCHUNKMESSAGE']._serialized_start=2803
  _globals['_REQUESTNEXTPRUNINGPOINTUTXOSETCHUNKMESSAGE']._serialized_end=2847
  _globals['_DONEPRUNINGPOINTUTXOSETCHUNKSMESSAGE']._serialized_start=2849
  _globals['_DONEPRUNINGPOINTUTXOSETCHUNKSMESSAGE']._serialized_end=2887
  _globals['_REQUESTIBDBLOCKSMESSAGE']._serialized_start=2889
  _globals['_REQUESTIBDBLOCKSMESSAGE']._serialized_end=2947
  _globals['_UNEXPECTEDPRUNINGPOINTMESSAGE']._serialized_start=2949
  _globals['_UNEXPECTEDPRUNINGPOINTMESSAGE']._serialized_end=2980
  _globals['_IBDBLOCKLOCATORMESSAGE']._serialized_start=2982
  _globals['_IBDBLOCKLOCATORMESSAGE']._serialized_end=3088
  _globals['_REQUESTIBDCHAINBLOCKLOCATORMESSAGE']._serialized_start=3090
  _globals['_REQUESTIBDCHAINBLOCKLOCATORMESSAGE']._serialized_end=3195
  _globals['_IBDCHAINBLOCKLOCATORMESSAGE']._serialized_start=3197
  _globals['_IBDCHAINBLOCKLOCATORMESSAGE']._serialized_end=3271
  _globals['_REQUESTANTICONEMESSAGE']._serialized_start=3273
  _globals['_REQUESTANTICONEMESSAGE']._serialized_end=3371
  _globals['_IBDBLOCKLOCATORHIGHESTHASHMESSAGE']._serialized_start=3373
  _globals['_IBDBLOCKLOCATORHIGHESTHASHMESSAGE']._serialized_end=3446
  _globals['_IBDBLOCKLOCATORHIGHESTHASHNOTFOUNDMESSAGE']._serialized_start=3448
  _globals['_IBDBLOCKLOCATORHIGHESTHASHNOTFOUNDMESSAGE']._serialized_end=3491
  _globals['_BLOCKHEADERSMESSAGE']._serialized_start=3493
  _globals['_BLOCKHEADERSMESSAGE']._serialized_end=3560
  _globals['_REQUESTPRUNINGPOINTANDITSANTICONEMESSAGE']._serialized_start=3562
  _globals['_REQUESTPRUNINGPOINTANDITSANTICONEMESSAGE']._serialized_end=3604
  _globals['_REQUESTNEXTPRUNINGPOINTANDITSANTICONEBLOCKSMESSAGE']._serialized_start=3606
  _globals['_REQUESTNEXTPRUNINGPOINTANDITSANTICONEBLOCKSMESSAGE']._serialized_end=3658
  _globals['_BLOCKWITHTRUSTEDDATAMESSAGE']._serialized_start=3661
  _globals['_BLOCKWITHTRUSTEDDATAMESSAGE']._serialized_end=3848
  _globals['_DAABLOCK']._serialized_start=3850
  _globals['_DAABLOCK']._serialized_end=3947
  _globals['_DAABLOCKV4']._serialized_start=3949
  _globals['_DAABLOCKV4']._serialized_end=4048
  _globals['_BLOCKGHOSTDAGDATAHASHPAIR']._serialized_start=4050
  _globals['_BLOCKGHOSTDAGDATAHASHPAIR']._serialized_end=4155
  _globals['_GHOSTDAGDATA']._serialized_start=4158
  _globals['_GHOSTDAGDATA']._serialized_end=4388
  _globals['_BLUESANTICONESIZES']._serialized_start=4390
  _globals['_BLUESANTICONESIZES']._serialized_end=4467
  _globals['_DONEBLOCKSWITHTRUSTEDDATAMESSAGE']._serialized_start=4469
  _globals['_DONEBLOCKSWITHTRUSTEDDATAMESSAGE']._serialized_end=4503
  _globals['_PRUNINGPOINTSMESSAGE']._serialized_start=4505
  _globals['_PRUNINGPOINTSMESSAGE']._serialized_end=4568
  _globals['_REQUESTPRUNINGPOINTPROOFMESSAGE']._serialized_start=4570
  _globals['_REQUESTPRUNINGPOINTPROOFMESSAGE']._serialized_end=4603
  _globals['_PRUNINGPOINTPROOFMESSAGE']._serialized_start=4605
  _globals['_PRUNINGPOINTPROOFMESSAGE']._serialized_end=4689
  _globals['_PRUNINGPOINTPROOFHEADERARRAY']._serialized_start=4691
  _globals['_PRUNINGPOINTPROOFHEADERARRAY']._serialized_end=4762
  _globals['_READYMESSAGE']._serialized_start=4764
  _globals['_READYMESSAGE']._serialized_end=4778
  _globals['_BLOCKWITHTRUSTEDDATAV4MESSAGE']._serialized_start=4780
  _globals['_BLOCKWITHTRUSTEDDATAV4MESSAGE']._serialized_end=4906
  _globals['_TRUSTEDDATAMESSAGE']._serialized_start=4908
  _globals['_TRUSTEDDATAMESSAGE']._serialized_end=5030
# @@protoc_insertion_point(module_scope)
