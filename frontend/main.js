$(document).ready(function() {
  // Animation setup
  $(".text").textillate({ loop: true, speed: 1500, sync: true, in: { effect: "bounceIn" }, out: { effect: "bounceOut" } });
  $(".siri-message").textillate({ loop: true, sync: true, in: { effect: "fadeInUp" }, out: { effect: "fadeOutUp" } });

  // Siri Wave setup
  const siriWave = new SiriWave({
      container: document.getElementById("siri-container"),
      width: 940,
      style: "ios9",
      amplitude: 1,
      speed: 0.3,
      height: 200,
      autostart: true,
      waveColor: "#ff0000",
      waveOffset: 0,
      rippleEffect: true,
      rippleColor: "#ffffff",
  });

  // Mic Button handler
  $("#MicBtn").click(async function() {
      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);

      try {
          const response = await eel.processCommand()();
          
          if(response.status === "success") {
              if(response.message === "awake") {
                  $(".assistant-status").text("Active");
                  $(".siri-message").text("How can I help you?");
              } else if(response.message === "sleep") {
                  $(".assistant-status").text("Standby");
                  $(".siri-message").text("Say 'Wake Up' to activate");
              }
          }
      } catch(error) {
          console.error("Error:", error);
          $(".siri-message").text("Connection error");
      } finally {
          $("#Oval").attr("hidden", false);
          $("#SiriWave").attr("hidden", true);
      }
  });
});
