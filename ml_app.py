import av
import cv2
from aiortc.contrib.media import MediaRecorder

from streamlit_webrtc import VideoProcessorBase, WebRtcMode, webrtc_streamer

act_lev = "Low"
def run_cap():
    class OpenCVEdgeProcessor(VideoProcessorBase):
        def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
            img = frame.to_ndarray(format="bgr24")

            # perform edge detection
            img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

            return av.VideoFrame.from_ndarray(img, format="bgr24")

    def in_recorder_factory() -> MediaRecorder:
        return MediaRecorder(
            "input.flv", format="flv"
        )  # HLS does not work. See https://github.com/aiortc/aiortc/issues/331

    def out_recorder_factory() -> MediaRecorder:
        return MediaRecorder("output.flv", format="flv")

    webrtc_streamer(
        key="loopback",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={
            "video": True,
            "audio": True,
        },
        video_processor_factory=OpenCVEdgeProcessor,
        in_recorder_factory=in_recorder_factory,
        out_recorder_factory=out_recorder_factory,
    )


run_cap()