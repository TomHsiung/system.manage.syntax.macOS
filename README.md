# system.manage.syntax.macOS
A collection of commonly used and useful system management command for macOS

# Contents
1) `osascript` is the syntax command to close an app via the terminal.
2) `RemoteManagement` is the syntax commands related to Remote Management.
3) `pmset` is the native command-line tool for power management of macOS.
4) `ssh` is the command to connect via SSH protocol.

# Supported encryption algorithm

|Algorithm|Description|
| - | - |
|rsa|an old algorithm based on the difficulty of factoring large numbers. A key size of at least 2048 bits is recommended for RSA; 4096 bits is better. RSA is getting old and significant advances are being made in factoring. Choosing a different algorithm may be advisable. It is quite possible the RSA algorithm will become practically breakable in the foreseeable future. All SSH clients support this algorithm.|
|dsa|an old US government Digital Signature Algorithm. It is based on the difficulty of computing discrete logarithms. A key size of 1024 would normally be used with it. DSA in its original form is no longer recommended.|
|ecdsa|a new Digital Signature Algorithm standarized by the US government, using elliptic curves. This is probably a good algorithm for current applications. Only three key sizes are supported: 256, 384, and 521 (sic!) bits. We would recommend always using it with 521 bits, since the keys are still small and probably more secure than the smaller keys (even though they should be safe as well). Most SSH clients now support this algorithm.|
|ed25519|this is a new algorithm added in OpenSSH. Support for it in clients is not yet universal. Thus its use in general purpose applications may not yet be advisable.|
