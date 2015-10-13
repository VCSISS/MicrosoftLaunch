<!doctype html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<title>Deploying a Windows 10 IoT App to Raspberry Pi 2</title>
		
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
		<script src="menu.js"></script>
		<script src="intro.js"></script>
	
		<link rel="stylesheet" href="style.css">	
		<link rel="stylesheet" href="style-instructions.css">
		
	</head>
	
	<body>
		
		<nav id="menu-container"></nav>
		
		<h1 id="header">Deploying a Windows 10 IoT Universal Windows Platform app to Raspberry Pi 2</h1>
		
		<p id="intro">
			This is a tutorial on how to use Visual Studio, C#/XAML, and Windows Powershell to build
			and deploy a UWP (Universal Windows Platform) app to a Raspberry Pi 2.
			<br>
			<br>
			This is a simplified version of these two sites:<br>
			http://ms-iot.github.io/content/en-US/win10/samples/HelloWorld.htm<br>
			http://ms-iot.github.io/content/en-US/win10/samples/PowerShell.htm<br>
			I do not claim to have created this content; I only rephrased it.
		</p>
		
		<div id="main">
			
			<dl id="main-list">
				
				<dt class="section-header">Hardware</dt>
					
				<dd>
					<dl>
						<dt class="section-separation">Requirements</dt>					
	
						<dd>
							<ol class="requirements">
								<li>Raspberry Pi 2</li>
							</ol>
						</dd>
						
						<dt class="section-separation">Instructions</dt>
						
						<dd class="instructions">
							<dl>
								<dt>Set up Raspberry Pi</dt>
								
								<dd>
									<ol class="instructions-ol">
										<li>Set it up</li>
									</ol>
								</dd>
							</dl>	
						</dd>
						
					</dl>
						
				</dd>
				
				<dt class="section-header">Software</dt>
					
				<dd>
			
					<dl>
						<dt class="section-separation">Requirements</dt>
						
						<dd>
						
							<ol class="requirements">
								<li>Visual Studio 2015 with Python UWP extensions</li>
								<li>Python 3x interpreter</li>
								<li>Windows Powershell</li>
							</ol>
							
						</dd>
						
						<dt class="section-separation">Instructions</dt>
								
						<dd>
							<dl class="instructions">

								<dt>
									Create new C# project
								</dt>
								
								<dd>
									<ol class="instructions-ol">
										<li>
											Open Visual Studio 2015
										</li>
										<li>
											Click File->New->Project
										</li>
										<li>
											Go to Templates->Visual C#->Windows->Universal
										</li>
										<li>
											Select "Blank App (Universal Windows)"
										</li>
										<li>
											Name it whatever you want
										</li>
										<li>
											Click Ok
										</li>
									</ol>

								</dd>

								<dt>
									Reference the Windows IoT SDK so that the app can run on the Windows IoT
								</dt>

								<dd>
									<ol class="instructions-ol">
										<li>
											On the right hand side of the window, right-click "References"
										</li>
										<li>
											Click "Add Reference"
										</li>
										<li>
											Click "Universal Windows"
										</li>
										<li>
											Click "Extensions"
										</li>
										<li>
											Double-click Windows IoT Extensions for the UWP
										</li>
										<li>
											Click Ok
										</li>
									</ol>

								</dd>

								<dt>
									Create the content of the App (sample Hello World app instructions given)
								</dt>
						
								<dd>
									<ol class="instructions-ol">
										<li>
											In the Solution Explorer, double-click on MainPage.xaml
										</li>
										<li>
											If you cannot find it, enter "MainPage.xaml" into the search bar
										</li>
										<li>
											Inside the <span class="code">&lt;Grid...&gt;...&lt;/Grid&gt;</span> tag, paste this code:
											<span class="code">&lt;TextBox Text="Hello, World!" Margin="10" IsReadOnly="True"
											HorizontalAlignment="Center" VerticalAlignment="Center"/&gt;</span>
											<br>
											<br>
											This code will create a text box that says "Hello, World!"
										</li>
										<li>
											Click BUILD->Build Solution
										</li>
										<li>
											Under output next to "Show output from: ", select "Build"
										</li>
										<li>
											If it says "Build Failed", look over your code. Try to fix any typos. It is suggested
											that you copy and paste the code. If you are certain that your code is correct, then try googling
											the error message.
										</li>
										<li>
											If it succeeded, then test your application by clicking the button that says "Device" near the top
											of the editor.
										</li>
										<li>
											If it asks you to install an emulator, click install
										</li>
										<li>
											If you cannot install an emulator, no worries. This was just to test if the app was working.
										</li>

									</ol>

								</dd>

								<dt>
									Start the Remote Debugger on the Raspberry Pi
								</dt>
								
								<dd>
									<ol class="instructions-ol">
										<li>
											Locate the Windows PowerShell app on your device
										</li>
										<li>
											Right-click it and click "Run as administrator"
										</li>
										<li>Enter your password</li>
										<li>Type <span class="code">net start WinRM</span></li>
										<li>Type <span class="code"> Set-Item WSMan:\localhost\Client\TrustedHosts -Value <machine-name or IP Address></span> without the less than and grater than signs</li>
										<li>Type <span class="code">Y</span></li>
										<li>Type <span class="code">Enter-PSSession -ComputerName <machine-name or IP Address> -Credential <machine-name or IP Address or localhost>\Administrator</span></li>
										<li>Enter the password (the default should be p@ssw0rd)</li>
										<li>After about 30 seconds, you should see a prompt that starts with the devices IP address. Success!</li>
									</ol>
									
									<p>For more help, see http://ms-iot.github.io/content/en-US/win10/samples/PowerShell.htm</p>

								</dd>

								<dt>
									Deploy the app
								</dt>
								
								<dd>
									<ol class="instructions-ol">
										<li>
											In the menu near the top that says "x86", select "ARM". Raspberry Pi uses the ARM architecture.
										</li>
										<li>
											Next to that dropdown menu, there should be a menu that says "Device" or "Local Machine". From that,
											select "Remote Machine".
										</li>
										<li>
											There should be a dialog titled "Remote Connections".  Enter the IP address (or machine name)
											of the Raspberry Pi and for "Authentication Mode", select "None".
										</li>
										<li>
											Click DEBUG->Start Debugging or "Remote Machine".
										</li>
										<li>You should now see the app on the monitor connected the the Raspberry Pi</li>
										<li>To stop the app, click DEBUG->Stop Debugging or press the little red square in the menu.</li>
									</ol>

								</dd>

								<dt>
									Set the app as the default app on the Windows IoT
								</dt>

								<dd>
									<ol class="instructions-ol">
										<li>
											There is a dropdown menu that contains the options "Debug" and "Release". Select "Release".
										</li>
										<li>
											In PowerShell, type <span class="code">iotstartup list HelloWorld</span>
											If you see something like <span class="code">Headed   : HelloWorld_n2pe7ts0w7wey!App</span>,
											then that means that the app was installed correctly.
										</li>
										<li>
											Type <span class="code">iotstartup add headed HelloWorld</span>.
											You should see <span class="code">AppId changed to HelloWorld_n2pe7ts0w7wey!App</span>.
										</li>
										<li>
											Restart your Windows IoT device: <span class="code">shutdown /r /t 0</span>
										</li>
										<li>
											You should now see the Hello, World app on startup.
										</li>
										<li>
											To change back to the default, type <span class="code">iotstartup add headed DefaultApp</span>
										</li>
									</ol>
								</dd>

							</dl>
					  </dd>
				</dl>
			
			</dl>
			
			<b>Works Cited:</b><br>
			<br>
			"Windows IoT - HelloWorld." Windows IoT - HelloWorld. N.p., n.d. Web. 10 Oct. 2015.<br>
			"Windows IoT - Use PowerShell to Connect to a Windows 10 IoT Core Device." <i>Windows IoT - Use PowerShell to Connect to a Windows 10 IoT Core Device.</i> N.p., n.d. Web. 10 Oct. 2015.
		</div>
		
	</body>
</html>