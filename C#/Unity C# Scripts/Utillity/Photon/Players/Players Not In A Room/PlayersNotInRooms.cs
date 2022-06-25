using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using Photon.Pun;

public class PlayersNotInRooms : MonoBehaviour
{
    //Refs
    public TMP_Text playersNotInRoom;
    private LoadBalancingClient loadBalancingClient;

    void Update()
    {
        playersNotInRoom.text = ("Players Not In A Room: " + loadBalancingClient.PlayersOnMasterCounts);
    }
}