from typing import List, Optional

from facefusion.typing import OutputAudioEncoder, OutputVideoEncoder, OutputVideoPreset, TempFrameFormat

# frame extraction
trim_frame_start : Optional[int] = None
trim_frame_end : Optional[int] = None
temp_frame_format : Optional[TempFrameFormat] = None
keep_temp : Optional[bool] = None
# output creation
output_image_quality : Optional[int] = None
output_image_resolution : Optional[str] = None
output_audio_encoder : Optional[OutputAudioEncoder] = None
output_video_encoder : Optional[OutputVideoEncoder] = None
output_video_preset : Optional[OutputVideoPreset] = None
output_video_quality : Optional[int] = None
output_video_resolution : Optional[str] = None
output_video_fps : Optional[float] = None
skip_audio : Optional[bool] = None
# frame processors
frame_processors : List[str] = []
# uis
open_browser : Optional[bool] = None
ui_layouts : List[str] = []
