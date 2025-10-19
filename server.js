// সহজ ভিডিও সার্ভার (video.mp4 সার্ভ করবে)
const express = require("express");
const fs = require("fs");
const app = express();

app.get("/video", (req, res) => {
  const path = "video.mp4";
  if (!fs.existsSync(path)) return res.status(404).send("Video not found");

  const stat = fs.statSync(path);
  res.writeHead(200, {
    "Content-Type": "video/mp4",
    "Content-Length": stat.size
  });
  fs.createReadStream(path).pipe(res);
});

app.listen(3000, () =>
  console.log("✅ সার্ভার চলছে: http://localhost:3000/video")
);
