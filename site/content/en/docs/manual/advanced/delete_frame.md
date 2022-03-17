---
title: 'Frame deleting'
linkTitle: 'Delete frame from task'
weight: 18
description: 'This section explains how delete and restore frame from task.'
---

# Delete frame

You can delete current frame from task. This frame will not be presented either in the UI or in the exported annotation.
Thus, it is possible to mark corrupted frames that are not subject to annotation.

1. Go to the Job annotation view and than click on the `Delete frame` button.

   ![](/images/image245.jpg)

1. After that you will be asked to confirm frame deleting.
   **Important note:**  all annotations from that frame will be deleted, unsaved annotations
   will be saved and the frame will be invisible in the annotation view (Until you make it visible in the settings).
   If there is some overlap in the task and the deleted frame falls within this interval,
   then this will cause this frame to become unavailable in another job as well.
1. When you delete a frame in a job with tracks, you may need adjust some tracks. Common adjustments are:
   - Add keyframes at the edges of the deleted interval in order for the interpolation to look correct;
   - Move keyframe start or end keyframe to the correct side of the deleted interval.

# Configurate deleted frames visability and navigation

If you need to enable showing the deleted frames, you can enable it in the settings.

1. Go to the settings and chose `Player` settings.

   ![](/images/image246.jpg)

1. Click on the `Show deleted frames` checkbox. And close the settings dialog.

   ![](/images/image247.jpg)

1. Then you will be able to navigate through deleted frames.
   But annotation tools will be unavailable. Deleted frames differ in the corresponding overlay.

1. There are view ways to navigate through deleted frames without enabling this option:
   - Go to the frame via direct navigation methods: navigation slider or frame input field,
   - Go to the frame via direct link.

1. Navigation with step will not count deleted frames.

# Restore deleted frame

You can also restore deleted frames in the task.

1. Turn on deleted frames visability, as it was told in the previous part,
   and go to the deleted frame you want to restore.

   ![](/images/image248.jpg)

2. Click on the `Restore` icon. The frame will be restored immediately.