
        document.addEventListener('DOMContentLoaded', function() {
            // DOM Elements
            const setupContainer = document.getElementById('setupContainer');
            const scorecardContainer = document.getElementById('scorecardContainer');
            const matchSetupSection = document.getElementById('matchSetup');
            const playerSelectionSection = document.getElementById('playerSelection');
            const nextBtn = document.getElementById('nextToPlayers');
            const backBtn = document.getElementById('backToSetup');
            const startBtn = document.getElementById('startMatch');
            const actionSection = document.getElementById('actionSection');
            const matchCompletedMsg = document.getElementById('matchCompletedMsg');
            const targetDisplay = document.getElementById('targetDisplay');
            const targetValue = document.getElementById('targetValue');
            
            // Form elements
            const hostInput = document.getElementById('host');
            const visitorInput = document.getElementById('visitor');
            const oversInput = document.getElementById('overs');
            const hostTossOption = document.getElementById('hostTossOption');
            const visitorTossOption = document.getElementById('visitorTossOption');
            const batOption = document.getElementById('batOption');
            const bowlOption = document.getElementById('bowlOption');
            const hostToss = document.getElementById('hostToss');
            const visitorToss = document.getElementById('visitorToss');
            const optedBat = document.getElementById('optedBat');
            const optedBowl = document.getElementById('optedBowl');
            const tossWinnerDisplay = document.getElementById('tossWinnerDisplay');
            const optedDisplay = document.getElementById('optedDisplay');
            const hostLabel = document.getElementById('hostTeamLabel');
            const visitorLabel = document.getElementById('visitorTeamLabel');
            
            // Info display elements
            const infoHost = document.getElementById('infoHost');
            const infoVisitor = document.getElementById('infoVisitor');
            const infoOvers = document.getElementById('infoOvers');
            const battingTeamDisplay = document.getElementById('battingTeamDisplay');
            const bowlingTeamDisplay = document.getElementById('bowlingTeamDisplay');
            
            // Player input fields
            const strikerInput = document.getElementById('striker');
            const nonStrikerInput = document.getElementById('nonStriker');
            const bowlerInput = document.getElementById('bowler');
            
            // Scorecard elements
            const matchTitle = document.getElementById('matchTitle');
            const currentInning = document.getElementById('currentInning');
            const totalRuns = document.getElementById('totalRuns');
            const currentOvers = document.getElementById('currentOvers');
            const runRate = document.getElementById('runRate');
            const battingTeamName = document.getElementById('battingTeamName');
            const crrDisplay = document.getElementById('crrDisplay');
            const batsmanBody = document.getElementById('batsmanBody');
            const bowlerBody = document.getElementById('bowlerBody');
            const overBallsContainer = document.getElementById('overBallsContainer');
            const overNumber = document.getElementById('overNumber');
            const newBatsmanForm = document.getElementById('newBatsmanForm');
            const newBatsmanInput = document.getElementById('newBatsman');
            const addBatsmanBtn = document.getElementById('addBatsman');
            const newBowlerForm = document.getElementById('newBowlerForm');
            const newBowlerInput = document.getElementById('newBowler');
            const addBowlerBtn = document.getElementById('addBowler');
            const secondInningSetup = document.getElementById('secondInningSetup');
            const secondStrikerInput = document.getElementById('secondStriker');
            const secondNonStrikerInput = document.getElementById('secondNonStriker');
            const secondBowlerInput = document.getElementById('secondBowler');
            const startSecondInningBtn = document.getElementById('startSecondInning');
            const matchResult = document.getElementById('matchResult');
            const resultText = document.getElementById('resultText');
            const firstInningTeam = document.getElementById('firstInningTeam');
            const firstInningScore = document.getElementById('firstInningScore');
            const secondInningTeam = document.getElementById('secondInningTeam');
            const secondInningScore = document.getElementById('secondInningScore');
            const manOfMatch = document.getElementById('manOfMatch');
            const toast = document.getElementById('toast');
            const currentPartnership = document.getElementById('currentPartnership');
            const bestPartnership = document.getElementById('bestPartnership');
            const currentRRR = document.getElementById('currentRRR');
            const requiredRRR = document.getElementById('requiredRRR');
            const wideCount = document.getElementById('wideCount');
            const noBallCount = document.getElementById('noBallCount');
            
            // New elements
            const backToScorecardBtn = document.getElementById('backToScorecardBtn');
            const newMatchBtn = document.getElementById('newMatchBtn');
            const backToSetupFromScorecard = document.getElementById('backToSetupFromScorecard');
            const restartMatchBtn = document.getElementById('restartMatchBtn');
            
            // Match state
            let matchData = {
                hostTeam: '',
                visitorTeam: '',
                totalOvers: 20,
                tossWinner: '',
                opted: '',
                inning: 1,
                battingTeam: '',
                bowlingTeam: '',
                striker: '',
                nonStriker: '',
                bowler: '',
                runs: 0,
                wickets: 0,
                balls: 0,
                extras: {
                    wide: 0,
                    noBall: 0,
                    byes: 0,
                    legByes: 0
                },
                batsmen: [
                    { name: '', runs: 0, balls: 0, fours: 0, sixes: 0, out: false },
                    { name: '', runs: 0, balls: 0, fours: 0, sixes: 0, out: false }
                ],
                bowlers: [
                    { name: '', overs: 0, maidens: 0, runs: 0, wickets: 0, balls: 0 }
                ],
                currentBowlerIndex: 0,
                team1Score: 0,
                team2Score: 0,
                team1Wickets: 0,
                team2Wickets: 0,
                target: 0,
                currentOver: [],
                ballHistory: [],
                partnerships: [],
                currentPartnershipRuns: 0,
                currentPartnershipBalls: 0,
                bestPartnershipRuns: 0,
                matchCompleted: false,
                firstInningBatting: [],
                firstInningBowling: [],
                secondInningBatting: [],
                secondInningBowling: []
            };
            
            // Initialize with default values
            hostLabel.textContent = hostInput.value;
            visitorLabel.textContent = visitorInput.value;
            tossWinnerDisplay.textContent = hostInput.value;
            
            // Show toast notification
            function showToast(message, duration = 3000) {
                toast.textContent = message;
                toast.classList.add('show');
                
                setTimeout(() => {
                    toast.classList.remove('show');
                }, duration);
            }
            
            // Update team labels when inputs change
            hostInput.addEventListener('input', function() {
                hostLabel.textContent = hostInput.value;
                updateTossDisplay();
            });
            
            visitorInput.addEventListener('input', function() {
                visitorLabel.textContent = visitorInput.value;
                updateTossDisplay();
            });
            
            // Toss selection
            hostTossOption.addEventListener('click', function() {
                hostToss.checked = true;
                updateTossDisplay();
            });
            
            visitorTossOption.addEventListener('click', function() {
                visitorToss.checked = true;
                updateTossDisplay();
            });
            
            // Opted selection
            batOption.addEventListener('click', function() {
                optedBat.checked = true;
                optedDisplay.textContent = 'BAT';
            });
            
            bowlOption.addEventListener('click', function() {
                optedBowl.checked = true;
                optedDisplay.textContent = 'BOWL';
            });
            
            // Update toss display
            function updateTossDisplay() {
                const tossWinner = hostToss.checked ? hostInput.value : visitorInput.value;
                tossWinnerDisplay.textContent = tossWinner;
            }
            
            // Next button - show player selection
            nextBtn.addEventListener('click', function() {
                // Update info displays
                infoHost.textContent = hostInput.value;
                infoVisitor.textContent = visitorInput.value;
                infoOvers.textContent = oversInput.value + ' overs';
                
                // Determine batting and bowling teams
                const tossWinner = hostToss.checked ? hostInput.value : visitorInput.value;
                const optedTo = optedBat.checked ? 'bat' : 'bowl';
                
                if ((hostToss.checked && optedTo === 'bat') || 
                    (visitorToss.checked && optedTo === 'bowl')) {
                    battingTeamDisplay.textContent = hostInput.value;
                    bowlingTeamDisplay.textContent = visitorInput.value;
                } else {
                    battingTeamDisplay.textContent = visitorInput.value;
                    bowlingTeamDisplay.textContent = hostInput.value;
                }
                
                // Switch sections
                matchSetupSection.classList.remove('active');
                playerSelectionSection.classList.add('active');
            });
            
            // Back button - return to match setup
            backBtn.addEventListener('click', function() {
                playerSelectionSection.classList.remove('active');
                matchSetupSection.classList.add('active');
            });
            
            // Start match button
            startBtn.addEventListener('click', function() {
                const striker = strikerInput.value.trim();
                const nonStriker = nonStrikerInput.value.trim();
                const bowler = bowlerInput.value.trim();
                
                if (!striker || !nonStriker || !bowler) {
                    showToast('Please enter all player names before starting the match.');
                    return;
                }
                
                if (striker === nonStriker) {
                    showToast('Striker and Non-Striker cannot be the same player.');
                    return;
                }
                
                // Store match data
                matchData = {
                    hostTeam: hostInput.value,
                    visitorTeam: visitorInput.value,
                    totalOvers: parseInt(oversInput.value),
                    tossWinner: hostToss.checked ? hostInput.value : visitorInput.value,
                    opted: optedBat.checked ? 'bat' : 'bowl',
                    inning: 1,
                    battingTeam: battingTeamDisplay.textContent,
                    bowlingTeam: bowlingTeamDisplay.textContent,
                    striker: striker,
                    nonStriker: nonStriker,
                    bowler: bowler,
                    runs: 0,
                    wickets: 0,
                    balls: 0,
                    extras: {
                        wide: 0,
                        noBall: 0,
                        byes: 0,
                        legByes: 0
                    },
                    batsmen: [
                        { name: striker, runs: 0, balls: 0, fours: 0, sixes: 0, out: false },
                        { name: nonStriker, runs: 0, balls: 0, fours: 0, sixes: 0, out: false }
                    ],
                    bowlers: [
                        { name: bowler, overs: 0, maidens: 0, runs: 0, wickets: 0, balls: 0 }
                    ],
                    currentBowlerIndex: 0,
                    team1Score: 0,
                    team2Score: 0,
                    team1Wickets: 0,
                    team2Wickets: 0,
                    target: 0,
                    currentOver: [],
                    ballHistory: [],
                    partnerships: [],
                    currentPartnershipRuns: 0,
                    currentPartnershipBalls: 0,
                    bestPartnershipRuns: 0,
                    matchCompleted: false,
                    firstInningBatting: [],
                    firstInningBowling: [],
                    secondInningBatting: [],
                    secondInningBowling: []
                };
                
                // Hide setup and show scorecard
                setupContainer.style.display = 'none';
                scorecardContainer.style.display = 'block';
                matchCompletedMsg.style.display = 'none';
                targetDisplay.style.display = 'none';
                backToSetupFromScorecard.style.display = 'block';
                restartMatchBtn.style.display = 'block';
                
                // Initialize scorecard
                updateScorecard();
                renderOverBalls();
                
                showToast('Match started! Good luck to both teams!');
            });
            
            // Render over balls horizontally
            function renderOverBalls() {
                overBallsContainer.innerHTML = '';
                matchData.currentOver.forEach(ball => {
                    const ballEl = document.createElement('div');
                    ballEl.className = 'over-ball';
                    
                    switch(ball.type) {
                        case 'wide':
                            ballEl.classList.add('wide');
                            ballEl.textContent = 'Wd';
                            break;
                        case 'noball':
                            ballEl.classList.add('noball');
                            ballEl.textContent = 'Nb';
                            break;
                        case 'wicket':
                            ballEl.classList.add('wicket');
                            ballEl.textContent = 'W';
                            break;
                        case 'run':
                            ballEl.textContent = ball.runs;
                            if (ball.runs === 4) ballEl.classList.add('four');
                            else if (ball.runs === 6) ballEl.classList.add('six');
                            else if (ball.runs === 0) ballEl.classList.add('zero');
                            else if (ball.runs === 1 || ball.runs === 3) ballEl.classList.add('one');
                            else if (ball.runs === 2 || ball.runs === 5) ballEl.classList.add('two');
                            break;
                    }
                    
                    overBallsContainer.appendChild(ballEl);
                });
            }
            
            // Update the scorecard display
            function updateScorecard() {
                // Update header information
                matchTitle.textContent = `${matchData.hostTeam} vs ${matchData.visitorTeam}`;
                currentInning.textContent = matchData.inning === 1 ? '1st Inning' : '2nd Inning';
                totalRuns.textContent = `${matchData.runs} / ${matchData.wickets}`;
                
                // Calculate overs
                const overs = Math.floor(matchData.balls / 6);
                const balls = matchData.balls % 6;
                currentOvers.textContent = `${overs}.${balls}`;
                
                // Calculate run rate
                const crr = matchData.balls > 0 ? (matchData.runs / (matchData.balls / 6)).toFixed(2) : '0.00';
                runRate.textContent = crr;
                crrDisplay.textContent = `CRR: ${crr}`;
                
                // Set batting team name
                battingTeamName.textContent = `${matchData.battingTeam} Batting`;
                battingTeamName.className = matchData.battingTeam === matchData.hostTeam ? 'india-bg' : 'australia-bg';
                
                // Update over number
                overNumber.textContent = `Over ${Math.floor(matchData.balls / 6) + 1}`;
                
                // Update batsman table
                batsmanBody.innerHTML = '';
                matchData.batsmen.forEach((batsman, index) => {
                    const sr = batsman.balls > 0 ? ((batsman.runs / batsman.balls) * 100).toFixed(2) : '0.00';
                    const row = document.createElement('tr');
                    
                    let status = 'Not Out';
                    if (batsman.out) status = 'Out';
                    
                    if (index === 0 && !batsman.out) {
                        row.innerHTML = `
                            <td class="striker">${batsman.name}</td>
                            <td>${batsman.runs}</td>
                            <td>${batsman.balls}</td>
                            <td>${batsman.fours}</td>
                            <td>${batsman.sixes}</td>
                            <td>${sr}</td>
                            <td>${status}</td>
                        `;
                    } else {
                        row.innerHTML = `
                            <td>${batsman.name}</td>
                            <td>${batsman.runs}</td>
                            <td>${batsman.balls}</td>
                            <td>${batsman.fours}</td>
                            <td>${batsman.sixes}</td>
                            <td>${sr}</td>
                            <td>${status}</td>
                        `;
                    }
                    
                    batsmanBody.appendChild(row);
                });
                
                // Update bowler table
                bowlerBody.innerHTML = '';
                const currentBowler = matchData.bowlers[matchData.currentBowlerIndex];
                const bowlerOvers = Math.floor(currentBowler.balls / 6);
                const bowlerBalls = currentBowler.balls % 6;
                const er = currentBowler.balls > 0 ? 
                    (currentBowler.runs / (currentBowler.balls / 6)).toFixed(2) : '0.00';
                
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${currentBowler.name}</td>
                    <td>${bowlerOvers}.${bowlerBalls}</td>
                    <td>${currentBowler.maidens}</td>
                    <td>${currentBowler.runs}</td>
                    <td>${currentBowler.wickets}</td>
                    <td>${er}</td>
                `;
                bowlerBody.appendChild(row);
                
                // Render over balls
                renderOverBalls();
                
                // Update analysis
                currentPartnership.textContent = `${matchData.currentPartnershipRuns} (${matchData.currentPartnershipBalls})`;
                bestPartnership.textContent = `${matchData.bestPartnershipRuns} runs`;
                wideCount.textContent = matchData.extras.wide;
                noBallCount.textContent = matchData.extras.noBall;
                
                if (matchData.inning === 2) {
                    targetDisplay.style.display = 'block';
                    targetValue.textContent = matchData.target;
                    
                    const remainingBalls = (matchData.totalOvers * 6) - matchData.balls;
                    const runsNeeded = matchData.target - matchData.runs;
                    
                    const currentRR = runsNeeded > 0 ? (runsNeeded / (remainingBalls / 6)).toFixed(2) : 0;
                    const requiredRR = runsNeeded > 0 ? (matchData.target / (matchData.totalOvers)).toFixed(2) : 0;
                    
                    currentRRR.textContent = currentRR;
                    requiredRRR.textContent = requiredRR;
                } else {
                    targetDisplay.style.display = 'none';
                }
                
                // Check for inning completion
                if (matchData.balls >= matchData.totalOvers * 6 || matchData.wickets >= 10) {
                    endInning();
                }
                
                // Check for win condition in second inning
                if (matchData.inning === 2 && matchData.runs >= matchData.target) {
                    endInning();
                }
            }
            
            // Run button functionality
            document.querySelectorAll('.run-btn').forEach(button => {
                button.addEventListener('click', function() {
                    if (matchData.matchCompleted) {
                        showToast('The match is already completed. No further actions allowed.');
                        return;
                    }
                    const runs = parseInt(this.getAttribute('data-runs'));
                    addRun(runs);
                });
            });
            
            // Add a run to the score
            function addRun(runs) {
                const currentBowler = matchData.bowlers[matchData.currentBowlerIndex];
                
                matchData.runs += runs;
                currentBowler.runs += runs;
                matchData.balls++;
                currentBowler.balls++;
                matchData.currentPartnershipRuns += runs;
                matchData.currentPartnershipBalls++;
                
                // Update batsman stats
                const strikerIndex = 0;
                matchData.batsmen[strikerIndex].runs += runs;
                matchData.batsmen[strikerIndex].balls++;
                
                if (runs === 4) matchData.batsmen[strikerIndex].fours++;
                if (runs === 6) matchData.batsmen[strikerIndex].sixes++;
                
                // Record ball
                matchData.currentOver.push({ type: 'run', runs: runs });
                matchData.ballHistory.push({ type: 'run', runs: runs });
                
                // Swap strike for odd runs
                if (runs % 2 === 1) {
                    swapStrike();
                }
                
                // Update best partnership
                if (matchData.currentPartnershipRuns > matchData.bestPartnershipRuns) {
                    matchData.bestPartnershipRuns = matchData.currentPartnershipRuns;
                }
                
                // Check for over completion (6 balls)
                if (matchData.currentOver.filter(b => b.type !== 'wide' && b.type !== 'noball').length >= 6) {
                    completeOver();
                }
                
                updateScorecard();
                showToast(`${matchData.striker} scored ${runs} run${runs === 1 ? '' : 's'}!`);
            }
            
            // Wide button
            document.getElementById('wideBtn').addEventListener('click', function() {
                if (matchData.matchCompleted) {
                    showToast('The match is already completed. No further actions allowed.');
                    return;
                }
                const currentBowler = matchData.bowlers[matchData.currentBowlerIndex];
                
                matchData.runs += 1;
                matchData.extras.wide += 1;
                currentBowler.runs += 1;
                matchData.currentPartnershipRuns += 1;
                
                // Record ball
                matchData.currentOver.push({ type: 'wide' });
                matchData.ballHistory.push({ type: 'wide' });
                
                // Update best partnership
                if (matchData.currentPartnershipRuns > matchData.bestPartnershipRuns) {
                    matchData.bestPartnershipRuns = matchData.currentPartnershipRuns;
                }
                
                updateScorecard();
                showToast('Wide ball! 1 run added to extras');
            });
            
            // No ball button
            document.getElementById('noBallBtn').addEventListener('click', function() {
                if (matchData.matchCompleted) {
                    showToast('The match is already completed. No further actions allowed.');
                    return;
                }
                const currentBowler = matchData.bowlers[matchData.currentBowlerIndex];
                
                matchData.runs += 1;
                matchData.extras.noBall += 1;
                currentBowler.runs += 1;
                matchData.currentPartnershipRuns += 1;
                
                // Record ball
                matchData.currentOver.push({ type: 'noball' });
                matchData.ballHistory.push({ type: 'noball' });
                
                // Update best partnership
                if (matchData.currentPartnershipRuns > matchData.bestPartnershipRuns) {
                    matchData.bestPartnershipRuns = matchData.currentPartnershipRuns;
                }
                
                updateScorecard();
                showToast('No ball! 1 run added to extras');
            });
            
            // Take a wicket
            document.getElementById('wicketBtn').addEventListener('click', function() {
                if (matchData.matchCompleted) {
                    showToast('The match is already completed. No further actions allowed.');
                    return;
                }
                takeWicket();
            });
            
            function takeWicket() {
                const currentBowler = matchData.bowlers[matchData.currentBowlerIndex];
                
                matchData.wickets++;
                currentBowler.wickets++;
                matchData.balls++;
                currentBowler.balls++;
                matchData.currentPartnershipBalls++;
                
                // Update batsman stats
                const strikerIndex = 0;
                matchData.batsmen[strikerIndex].out = true;
                
                // Record partnership
                matchData.partnerships.push({
                    runs: matchData.currentPartnershipRuns,
                    balls: matchData.currentPartnershipBalls,
                    batsmen: [matchData.striker, matchData.nonStriker]
                });
                
                // Reset partnership
                matchData.currentPartnershipRuns = 0;
                matchData.currentPartnershipBalls = 0;
                
                // Record ball
                matchData.currentOver.push({ type: 'wicket' });
                matchData.ballHistory.push({ type: 'wicket' });
                
                // Show new batsman form
                newBatsmanForm.style.display = 'block';
                
                updateScorecard();
                showToast(`${matchData.striker} is out!`);
            }
            
            // Swap strike between batsmen
            document.getElementById('swapBtn').addEventListener('click', function() {
                if (matchData.matchCompleted) {
                    showToast('The match is already completed. No further actions allowed.');
                    return;
                }
                swapStrike();
            });
            
            function swapStrike() {
                // Swap batsmen in the array
                [matchData.batsmen[0], matchData.batsmen[1]] = [matchData.batsmen[1], matchData.batsmen[0]];
                [matchData.striker, matchData.nonStriker] = [matchData.nonStriker, matchData.striker];
                updateScorecard();
                showToast('Batsmen swapped positions!');
            }
            
            // Complete over
            function completeOver() {
                // Swap batsmen at end of over
                swapStrike();
                
                // Record partnership
                matchData.partnerships.push({
                    runs: matchData.currentPartnershipRuns,
                    balls: matchData.currentPartnershipBalls,
                    batsmen: [matchData.striker, matchData.nonStriker]
                });
                
                // Reset current over
                matchData.currentOver = [];
                
                // Reset partnership
                matchData.currentPartnershipRuns = 0;
                matchData.currentPartnershipBalls = 0;
                
                // Only show new bowler form if the inning is not ending
                if (matchData.balls < matchData.totalOvers * 6 && matchData.wickets < 10) {
                    newBowlerForm.style.display = 'block';
                    showToast('Over completed!');
                } else {
                    showToast('Over completed! Inning ended.');
                }
            }
            
            // Add new batsman
            addBatsmanBtn.addEventListener('click', function() {
                const newBatsman = newBatsmanInput.value.trim();
                if (!newBatsman) {
                    showToast('Please enter a batsman name');
                    return;
                }
                
                // Find the out batsman and replace
                const outIndex = matchData.batsmen.findIndex(b => b.out);
                if (outIndex !== -1) {
                    matchData.batsmen[outIndex] = {
                        name: newBatsman,
                        runs: 0,
                        balls: 0,
                        fours: 0,
                        sixes: 0,
                        out: false
                    };
                    
                    // Update striker if needed
                    if (outIndex === 0) {
                        matchData.striker = newBatsman;
                    } else {
                        matchData.nonStriker = newBatsman;
                    }
                }
                
                // Hide form
                newBatsmanForm.style.display = 'none';
                newBatsmanInput.value = '';
                
                updateScorecard();
                showToast(`${newBatsman} is the new batsman!`);
            });
            
            // Add new bowler
            addBowlerBtn.addEventListener('click', function() {
                const newBowlerName = newBowlerInput.value.trim();
                if (!newBowlerName) {
                    showToast('Please enter a bowler name');
                    return;
                }
                
                // Check if bowler already exists
                let bowlerIndex = matchData.bowlers.findIndex(b => b.name === newBowlerName);
                
                if (bowlerIndex === -1) {
                    // Add new bowler
                    matchData.bowlers.push({
                        name: newBowlerName,
                        overs: 0,
                        maidens: 0,
                        runs: 0,
                        wickets: 0,
                        balls: 0
                    });
                    bowlerIndex = matchData.bowlers.length - 1;
                }
                
                // Set new bowler
                matchData.currentBowlerIndex = bowlerIndex;
                matchData.bowler = newBowlerName;
                
                // Hide form
                newBowlerForm.style.display = 'none';
                newBowlerInput.value = '';
                
                updateScorecard();
                showToast(`${newBowlerName} is the new bowler!`);
            });
            
            // Start second inning
            startSecondInningBtn.addEventListener('click', function() {
                const striker = secondStrikerInput.value.trim();
                const nonStriker = secondNonStrikerInput.value.trim();
                const bowler = secondBowlerInput.value.trim();
                
                if (!striker || !nonStriker || !bowler) {
                    showToast('Please enter all player names for the second inning.');
                    return;
                }
                
                if (striker === nonStriker) {
                    showToast('Striker and Non-Striker cannot be the same player.');
                    return;
                }
                
                // Save first inning data
                matchData.firstInningBatting = [...matchData.batsmen];
                matchData.firstInningBowling = [...matchData.bowlers];
                
                // Set players for second inning
                matchData.striker = striker;
                matchData.nonStriker = nonStriker;
                matchData.bowler = bowler;
                
                // Reset batsmen
                matchData.batsmen = [
                    { name: striker, runs: 0, balls: 0, fours: 0, sixes: 0, out: false },
                    { name: nonStriker, runs: 0, balls: 0, fours: 0, sixes: 0, out: false }
                ];
                
                // Reset bowlers
                matchData.bowlers = [
                    { name: bowler, overs: 0, maidens: 0, runs: 0, wickets: 0, balls: 0 }
                ];
                matchData.currentBowlerIndex = 0;
                
                // Reset partnership
                matchData.currentPartnershipRuns = 0;
                matchData.currentPartnershipBalls = 0;
                matchData.partnerships = [];
                
                // Reset score
                matchData.runs = 0;
                matchData.wickets = 0;
                matchData.balls = 0;
                matchData.extras.wide = 0;
                matchData.extras.noBall = 0;
                matchData.currentOver = [];
                matchData.ballHistory = [];
                
                // Hide setup form
                secondInningSetup.style.display = 'none';
                
                updateScorecard();
                showToast('Second inning started!');
            });
            
            // Undo last ball
            document.getElementById('undoBtn').addEventListener('click', function() {
                if (matchData.matchCompleted) {
                    showToast('The match is already completed. No further actions allowed.');
                    return;
                }
                undoLastBall();
            });
            
            function undoLastBall() {
                if (matchData.ballHistory.length === 0) {
                    showToast('No actions to undo');
                    return;
                }
                
                const lastBall = matchData.ballHistory.pop();
                const currentBowler = matchData.bowlers[matchData.currentBowlerIndex];
                
                // Remove from current over if it's the last ball
                if (matchData.currentOver.length > 0) {
                    matchData.currentOver.pop();
                }
                
                // Revert runs
                if (lastBall.type === 'run') {
                    matchData.runs -= lastBall.runs;
                    currentBowler.runs -= lastBall.runs;
                    matchData.balls--;
                    currentBowler.balls--;
                    matchData.currentPartnershipRuns -= lastBall.runs;
                    matchData.currentPartnershipBalls--;
                    
                    // Update batsman stats
                    const strikerIndex = 0;
                    matchData.batsmen[strikerIndex].runs -= lastBall.runs;
                    matchData.batsmen[strikerIndex].balls--;
                    
                    if (lastBall.runs === 4) matchData.batsmen[strikerIndex].fours--;
                    if (lastBall.runs === 6) matchData.batsmen[strikerIndex].sixes--;
                    
                    // Revert strike swap for odd runs
                    if (lastBall.runs % 2 === 1) {
                        swapStrike();
                    }
                } 
                else if (lastBall.type === 'wide' || lastBall.type === 'noball') {
                    matchData.runs -= 1;
                    currentBowler.runs -= 1;
                    matchData.currentPartnershipRuns -= 1;
                    
                    if (lastBall.type === 'wide') matchData.extras.wide--;
                    if (lastBall.type === 'noball') matchData.extras.noBall--;
                } 
                else if (lastBall.type === 'wicket') {
                    matchData.wickets--;
                    currentBowler.wickets--;
                    matchData.balls--;
                    currentBowler.balls--;
                    matchData.currentPartnershipBalls--;
                    
                    // Reset batsman out status
                    const strikerIndex = 0;
                    matchData.batsmen[strikerIndex].out = false;
                    newBatsmanForm.style.display = 'none';
                    
                    // Restore partnership
                    const lastPartnership = matchData.partnerships.pop();
                    if (lastPartnership) {
                        matchData.currentPartnershipRuns = lastPartnership.runs;
                        matchData.currentPartnershipBalls = lastPartnership.balls;
                    }
                }
                
                updateScorecard();
                showToast('Last action undone');
            }
            
            // End of inning
            function endInning() {
                if (matchData.inning === 1) {
                    // Set target for second inning
                    matchData.target = matchData.runs + 1;
                    matchData.team1Score = matchData.runs;
                    matchData.team1Wickets = matchData.wickets;
                    
                    // Save first inning data
                    matchData.firstInningBatting = [...matchData.batsmen];
                    matchData.firstInningBowling = [...matchData.bowlers];
                    
                    // Switch to second inning
                    matchData.inning = 2;
                    matchData.battingTeam = matchData.bowlingTeam;
                    matchData.bowlingTeam = matchData.battingTeam;
                    matchData.runs = 0;
                    matchData.wickets = 0;
                    matchData.balls = 0;
                    matchData.extras.wide = 0;
                    matchData.extras.noBall = 0;
                    
                    // Reset partnership
                    matchData.currentPartnershipRuns = 0;
                    matchData.currentPartnershipBalls = 0;
                    matchData.partnerships = [];
                    
                    // Hide player forms and show second inning setup
                    newBatsmanForm.style.display = 'none';
                    newBowlerForm.style.display = 'none';
                    secondInningSetup.style.display = 'block';
                    
                    showToast(`Inning break! ${matchData.bowlingTeam} needs ${matchData.target} runs to win.`);
                } else {
                    // Match completed
                    matchData.team2Score = matchData.runs;
                    matchData.team2Wickets = matchData.wickets;
                    
                    // Save second inning data
                    matchData.secondInningBatting = [...matchData.batsmen];
                    matchData.secondInningBowling = [...matchData.bowlers];
                    
                    // Determine winner
                    let winner = '';
                    let winMargin = '';
                    
                    if (matchData.team1Score > matchData.team2Score) {
                        // Team 1 wins
                        winner = matchData.bowlingTeam;
                        winMargin = `${matchData.team1Score - matchData.team2Score} runs`;
                        resultText.textContent = `${winner} wins by ${winMargin}!`;
                    } else if (matchData.team1Score < matchData.team2Score) {
                        // Team 2 wins
                        winner = matchData.battingTeam;
                        const wicketsLeft = 10 - matchData.wickets;
                        winMargin = `${wicketsLeft} wicket${wicketsLeft === 1 ? '' : 's'}`;
                        resultText.textContent = `${winner} wins by ${winMargin}!`;
                    } else {
                        // Tie
                        resultText.textContent = 'Match Tied!';
                    }
                    
                    // Set team scores
                    firstInningTeam.textContent = `${matchData.hostTeam === matchData.bowlingTeam ? matchData.visitorTeam : matchData.hostTeam}`;
                    firstInningScore.textContent = `${matchData.team1Score}/${matchData.team1Wickets}`;
                    
                    secondInningTeam.textContent = `${matchData.hostTeam === matchData.battingTeam ? matchData.visitorTeam : matchData.hostTeam}`;
                    secondInningScore.textContent = `${matchData.team2Score}/${matchData.team2Wickets}`;
                    
                    // Set man of the match
                    const topScorer = [...matchData.batsmen].sort((a, b) => b.runs - a.runs)[0];
                    manOfMatch.textContent = topScorer.name;
                    
                    // Show match result
                    matchResult.style.display = 'block';
                    
                    // Set match as completed
                    matchData.matchCompleted = true;
                    matchCompletedMsg.style.display = 'block';
                    actionSection.classList.add('disabled');
                }
                
                updateScorecard();
            }
            
            // Back to scorecard button in match result
            backToScorecardBtn.addEventListener('click', function() {
                matchResult.style.display = 'none';
            });
            
            // Start new match button
            newMatchBtn.addEventListener('click', function() {
                // Reset all forms and show the initial setup
                setupContainer.style.display = 'block';
                scorecardContainer.style.display = 'none';
                matchSetupSection.classList.add('active');
                playerSelectionSection.classList.remove('active');
                matchResult.style.display = 'none';
                backToSetupFromScorecard.style.display = 'none';
                restartMatchBtn.style.display = 'none';
                
                // Reset form values
                hostInput.value = 'India';
                visitorInput.value = 'Australia';
                oversInput.value = '20';
                hostToss.checked = true;
                optedBat.checked = true;
                strikerInput.value = 'Virat Kohli';
                nonStrikerInput.value = 'Rohit Sharma';
                bowlerInput.value = 'Pat Cummins';
                
                // Update displays
                updateTossDisplay();
                showToast('Ready to start a new match!');
            });
            
            // Back to setup from scorecard
            backToSetupFromScorecard.addEventListener('click', function() {
                setupContainer.style.display = 'block';
                scorecardContainer.style.display = 'none';
                backToSetupFromScorecard.style.display = 'none';
                restartMatchBtn.style.display = 'none';
            });
            
            // Restart match button
            restartMatchBtn.addEventListener('click', function() {
                if (confirm('Are you sure you want to restart the current match? All progress will be lost.')) {
                    // Reset match data
                    matchData = {
                        hostTeam: hostInput.value,
                        visitorTeam: visitorInput.value,
                        totalOvers: parseInt(oversInput.value),
                        tossWinner: hostToss.checked ? hostInput.value : visitorInput.value,
                        opted: optedBat.checked ? 'bat' : 'bowl',
                        inning: 1,
                        battingTeam: battingTeamDisplay.textContent,
                        bowlingTeam: bowlingTeamDisplay.textContent,
                        striker: strikerInput.value,
                        nonStriker: nonStrikerInput.value,
                        bowler: bowlerInput.value,
                        runs: 0,
                        wickets: 0,
                        balls: 0,
                        extras: {
                            wide: 0,
                            noBall: 0,
                            byes: 0,
                            legByes: 0
                        },
                        batsmen: [
                            { name: strikerInput.value, runs: 0, balls: 0, fours: 0, sixes: 0, out: false },
                            { name: nonStrikerInput.value, runs: 0, balls: 0, fours: 0, sixes: 0, out: false }
                        ],
                        bowlers: [
                            { name: bowlerInput.value, overs: 0, maidens: 0, runs: 0, wickets: 0, balls: 0 }
                        ],
                        currentBowlerIndex: 0,
                        team1Score: 0,
                        team2Score: 0,
                        team1Wickets: 0,
                        team2Wickets: 0,
                        target: 0,
                        currentOver: [],
                        ballHistory: [],
                        partnerships: [],
                        currentPartnershipRuns: 0,
                        currentPartnershipBalls: 0,
                        bestPartnershipRuns: 0,
                        matchCompleted: false,
                        firstInningBatting: [],
                        firstInningBowling: [],
                        secondInningBatting: [],
                        secondInningBowling: []
                    };
                    
                    // Hide forms and messages
                    newBatsmanForm.style.display = 'none';
                    newBowlerForm.style.display = 'none';
                    secondInningSetup.style.display = 'none';
                    matchResult.style.display = 'none';
                    matchCompletedMsg.style.display = 'none';
                    actionSection.classList.remove('disabled');
                    
                    // Update scorecard
                    updateScorecard();
                    renderOverBalls();
                    
                    showToast('Match restarted!');
                }
            });
            
            // Initialize display
            updateTossDisplay();
        });
    