from ttn import ApplicationClient
from utils import stubs
import grpc
import github_com.TheThingsNetwork.api.handler.handler_pb2 as proto
import github_com.TheThingsNetwork.api.handler.handler_pb2_grpc as handler


def test_application_constructor():
    appclient = ApplicationClient(stubs.apptest['appId'], stubs.apptest['accessKey'], stubs.handlerAddress, stubs.handler['certificate'])
    assert hasattr(appclient, 'app_access_key')

def test__application_constructor_token():
    appclient = ApplicationClient(stubs.apptest['appId'], stubs.apptest['accessToken'])
    assert hasattr(appclient, 'app_access_token')

def test_application_get():
    appclient = ApplicationClient('test-application-manager', 'ttn-account-v2.kSlfInIu4-V9t9A1k-SZVy0SlT8X1Y3VnoHaHSx1mXE')
    app = appclient.get()
    assert app.app_id == 'test-application-manager'

def test_application_devices():
    appclient = ApplicationClient('test-application-manager', 'ttn-account-v2.kSlfInIu4-V9t9A1k-SZVy0SlT8X1Y3VnoHaHSx1mXE')
    devices = appclient.devices()
    assert not devices

def test_set_payload_format():
    appclient = ApplicationClient('test-application-manager', 'ttn-account-v2.kSlfInIu4-V9t9A1k-SZVy0SlT8X1Y3VnoHaHSx1mXE')
    appclient.set_payload_format('payloadformat')
    app = appclient.get()
    assert app.payload_format == 'payloadformat'

def test_set_custom_payload():
    appclient = ApplicationClient('test-application-manager', 'ttn-account-v2.kSlfInIu4-V9t9A1k-SZVy0SlT8X1Y3VnoHaHSx1mXE')
    appclient.set_custom_payload_functions(validator="validator", decoder="decoder")
    app = appclient.get()
    assert app.payload_format == "custom" and app.decoder=="decoder" and app.validator == "validator"

def test_set_register_on_join_access_key():
    appclient = ApplicationClient('test-application-manager', 'ttn-account-v2.kSlfInIu4-V9t9A1k-SZVy0SlT8X1Y3VnoHaHSx1mXE')
    appclient.set_register_on_join_access_key('register')
    app = appclient.get()
    assert app.register_on_join_access_key == 'register'

def test_register_device():
    appclient = ApplicationClient('test-application-manager', 'ttn-account-v2.kSlfInIu4-V9t9A1k-SZVy0SlT8X1Y3VnoHaHSx1mXE')
    appclient.register_device("foo", stubs.devicetest)

def test_device():
    appclient = ApplicationClient('test-application-manager', 'ttn-account-v2.kSlfInIu4-V9t9A1k-SZVy0SlT8X1Y3VnoHaHSx1mXE')
    device = appclient.device('foo')
    assert device.dev_id == "foo"

def test_update_device():
    appclient = ApplicationClient('test-application-manager', 'ttn-account-v2.kSlfInIu4-V9t9A1k-SZVy0SlT8X1Y3VnoHaHSx1mXE')
    update = {
        "devEui": "1100223344556677",
    }
    appclient.update_device('foo', update)
    dev = appclient.device('foo')
    assert dev.lorawan_device.dev_eui == "1100223344556677".decode("hex")

def test_delete_device():
    appclient = ApplicationClient('test-application-manager', 'ttn-account-v2.kSlfInIu4-V9t9A1k-SZVy0SlT8X1Y3VnoHaHSx1mXE')
    appclient.delete_device("foo")
    devices = appclient.devices()
    assert not devices
