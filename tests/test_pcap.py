from chepy import Chepy


def test_pcap_dns():
    assert (
        len(
            Chepy("tests/files/test.pcapng")
            .debug(True)
            .read_pcap()
            .pcap_dns_queries()
            .set()
            .o
        )
        == 3
    )


def test_pcap_http_streams():
    assert len(Chepy("tests/files/test.pcapng").read_pcap().pcap_http_streams().o) == 4


def test_pcap_payload():
    assert Chepy("tests/files/test.pcapng").read_pcap().pcap_payload(
        layer="ICMP"
    ).o == [b"secret", b"message"]


def test_packet_to_dict():
    assert (
        Chepy("tests/files/test.pcapng").read_pcap().pcap_to_dict().o[0]["IP"]["src"]
        == "10.10.10.11"
    )
