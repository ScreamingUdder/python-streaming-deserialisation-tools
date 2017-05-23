import EventSchema42.EventMessage as EventMessage
import EventSchema42.FacilityData as FacilityData
from EventSchema42.ISISData import ISISData
from EventSchema42.RunState import RunState


class EventDeserialiser42(object):
    """
    Deserialisation for event data encoded with the f42 schema.
    """

    @staticmethod
    def deserialise_data(buf):
        """
        Extract event data from FlatBuffers encoded data.

        :param buf: the FlatBuffers data buffer as a bytearray
        :return: a dictionary containing the relevant information
        """
        ans = EventMessage.EventMessage.GetRootAsEventMessage(buf, 0)

        data = dict()
        data["source_name"] = ans.SourceName()
        data["message_id"] = ans.MessageId()
        data["pulse_time"] = ans.PulseTime()

        det_ids = list()
        for i in range(ans.DetectorIdLength()):
            det_ids.append(ans.DetectorId(i))
        data["det_ids"] = det_ids

        tofs = list()
        for i in range(ans.TimeOfFlightLength()):
            tofs.append(ans.TimeOfFlight(i))
        data["tofs"] = tofs

        d = ans.FacilitySpecificDataType()

        if ans.FacilitySpecificDataType() == FacilityData.FacilityData.ISISData:
            isis_data = ISISData()
            isis_data.Init(ans.FacilitySpecificData().Bytes, ans.FacilitySpecificData().Pos)
            data["period"] = isis_data.PeriodNumber()
            data["proton_charge"] = isis_data.ProtonCharge()
            if isis_data.RunState() == RunState.SETUP:
                data["run_state"] = "SETUP"
            elif isis_data.RunState() == RunState.RUNNING:
                data["run_state"] = "RUNNING"

        return data
