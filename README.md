# CloudBackup
###Bitcoin Authenticator cloud backup
A django implementation of a cloud pseudonymous wallet meta-data backup scheme.

####Problem:
 bitcoin authenticator uses a bip44 like hierarchy of accounts to handle its keys.<br>
An account can be a standard Pay-To_PubHash account where redeeming coins require only a single key pair <b>or</b> a paired account which is a Pay-To-Hash account where redeeming coins require both the wallet’s<br>
key pair and a second key pair generated on a different device (the authenticator).<br>
Other account types could be created in the future.<br>
Such a scheme creates a problem when the wallet needs to be restored only from its seed, the user needs to remember the precise index of the different accounts and the exact paired devices.
 
####Non scalable work around:
 the user is required to remember the indexes and reconstruct
 all accounts when restoring from seed.<br>
 
####Cloud Solution:
An anonymous cloud back-up scheme that stores all the necessary wallet meta data, encrypted, automatically.
####When POSTING a dump of the wallet's meta-data:
 <ol>
      <li>A new user is created in the server (username + password, email activation)</li>
      <li>The user logs in to the service</li>
      <li>The user creates a new wallet associated with him (can have more than one wallet), with a unique identifier H(seed).</li>
       <li>A dump of all the accounts + pairing data is serialised to a byte array (the payload) + checksum</li>
       <li>The wallet derives the cloud backup encryption key, following<br> <b>m / 100' / 0' / 0' / 0 / 1</b></li>
       <li>The wallet encrypts the payload with the derived cloud backup encryption key to create the <b>encryptedPayload</b></li>
       <li>the <b>encryptedPayload</b> is posted to the cloud service</li>
       <li>every change in the account hierarchy will trigger an update which will run through stages 4-7.</li>
  </ol>

####When restoring:
  <ol>
  <li>The user enters the seed (mnemonics, QR, SSS, etc.) </li> 
  <li>User loges into the service with its username and password </li>
  <li>User asks for the latest wallet meta-data encrypted dump with a GET request to the server</li>
  <li>The wallet derives the cloud backup encryption key, following<br> <b>m / 100' / 0' / 0' / 0 / 1</b></li>
  <li>Wallet decrypts the downloaded payload and uses it to restore the wallet</li>
  </ol>

####What exactly the dump consists of?
The dump can consist, as a minimum, the pairing and accounts info and can be extended to include: transaction history, SPV chain data, bloom filters, etc.