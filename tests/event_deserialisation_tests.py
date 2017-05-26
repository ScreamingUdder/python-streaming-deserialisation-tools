import unittest
from deserialisers.event_deserialisation import EventDeserialiser42


class TestEventDeserialiser42(unittest.TestCase):
    def setUp(self):
        with open('example_event_42', 'rb') as f:
            buf = f.read()
            self.data = EventDeserialiser42.deserialise_data(buf)
            print self.data

    def test_deserialise_pulse_time_correctly(self):
        self.assertEqual(1460431748833007813, self.data['pulse_time'])

    def test_deserialise_source_name_correctly(self):
        self.assertEqual('isis_nexus_streamer_for_mantid', self.data['source_name'])

    def test_deserialise_tofs_correctly(self):
        self.assertEqual(749, len(self.data['tofs']))
        self.assertEqual(11753951, self.data['tofs'][0])

    def test_deserialise_det_ids_correctly(self):
        self.assertEqual(749, len(self.data['det_ids']))
        self.assertEqual(63664, self.data['det_ids'][0])

    def test_deserialise_message_id_correctly(self):
        self.assertEqual(18130, self.data['message_id'])

    def test_deserialise_run_state_correctly(self):
        self.assertEqual('RUNNING', self.data['run_state'])

    def test_deserialise_period_correctly(self):
        self.assertEqual(0, self.data['period'])

    def test_deserialise_proton_charge_correctly(self):
        self.assertEqual(0.0011053680209442973, self.data['proton_charge'])
